#!/usr/bin/env python3
"""
Cyber Safer — Interactive cybersecurity training through AI-powered scenarios.

Run:
  uvicorn cybers:app --reload --port 8021
Then open http://localhost:8021/
"""

import os, re, json, torch, threading
from typing import Optional, Dict, Any, AsyncGenerator, List
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import (
    AutoTokenizer, AutoModelForCausalLM,
    TextIteratorStreamer, BitsAndBytesConfig
)

# ---------- Models ----------

class ScenarioState(BaseModel):
    """Track progress through a scenario."""
    scenario_id: str
    user_responses: List[str] = []
    ai_responses: List[str] = []
    red_flags_detected: List[str] = []
    score: int = 0
    completed: bool = False

# ---------- Quantization helpers ----------

def build_bnb(bits: Optional[int]):
    if not bits:
        return None
    if bits == 4:
        return BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
        )
    if bits == 8:
        return BitsAndBytesConfig(load_in_8bit=True)
    raise ValueError("--bits must be 4, 8, or omitted")

def _first_word(name: Optional[str], default="Assistant") -> str:
    if not name:
        return default
    return re.sub(r"[^A-Za-z0-9_.\\-]", "", name.strip().split()[0]) or default

# ---------- Player loader ----------

def load_player(path_or_name: str, base_dir: str = "players") -> Dict[str, Any]:
    """Load a persona ('player') JSON either by path or short name."""
    if not path_or_name:
        return {}
    if os.path.isfile(path_or_name):
        path = path_or_name
    else:
        guess = os.path.join(base_dir, f"{path_or_name}.json")
        path = guess if os.path.isfile(guess) else path_or_name
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️  Could not load player '{path_or_name}': {e}")
        return {}

# ---------- Scenario loader ----------

def load_scenarios(scenarios_dir: str = "scenarios") -> Dict[str, Dict[str, Any]]:
    """Load all scenario JSON files from directory."""
    scenarios = {}
    
    if not os.path.exists(scenarios_dir):
        print(f"⚠️  Scenarios directory '{scenarios_dir}' not found")
        return scenarios
    
    for filename in os.listdir(scenarios_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(scenarios_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    scenario = json.load(f)
                    scenario_id = scenario.get("id", filename[:-5])
                    scenarios[scenario_id] = scenario
                    print(f"📚 Loaded scenario: {scenario.get('title', scenario_id)}")
            except Exception as e:
                print(f"⚠️  Failed to load {filename}: {e}")
    
    return scenarios

# ---------- Red flag detection ----------

def detect_red_flags(user_message: str, red_flags: List[str]) -> List[str]:
    """Simple keyword-based red flag detection."""
    detected = []
    message_lower = user_message.lower()
    
    # Red flag keywords mapping
    flag_keywords = {
        "questions_sender": ["who are you", "who is this", "verify", "prove", "real", "legitimate", "are you really"],
        "refuses_to_click": ["won't click", "not clicking", "don't trust", "suspicious link", "not opening", "won't open"],
        "checks_url": ["url", "link", "address", "domain", "website"],
        "reports_phishing": ["report", "spam", "phishing", "scam", "reporting"],
        "questions_urgency": ["why urgent", "why now", "what happens if", "why 24 hours", "why immediate"],
        "asks_for_proof": ["proof", "evidence", "show me", "verify", "confirm"],
        "refuses_money": ["no money", "won't pay", "not sending", "can't afford", "won't give"],
        "blocks_contact": ["block", "blocking you", "stop contacting", "leave me alone"],
        "tells_adult": ["tell parent", "tell teacher", "get help", "talk to adult", "ask parent"],
        "questions_personal_info": ["why do you need", "why personal", "don't give info"],
        "recognizes_manipulation": ["manipulating", "trying to trick", "not fair", "guilt trip"],
        "verifies_independently": ["check myself", "look it up", "verify elsewhere", "call them directly"]
    }
    
    for flag in red_flags:
        keywords = flag_keywords.get(flag, [flag.replace("_", " ")])
        if any(keyword in message_lower for keyword in keywords):
            detected.append(flag)
    
    return detected

# ---------- Scoring ----------

def calculate_scenario_score(state: ScenarioState, scenario: Dict[str, Any]) -> int:
    """Calculate score based on red flags detected and responses."""
    base_score = 0
    
    # Points for detecting red flags (20 points each)
    required_flags = scenario.get("success_criteria", [])
    for flag in state.red_flags_detected:
        if flag in required_flags:
            base_score += 20
    
    # Bonus for number of good responses (up to 30 points)
    base_score += min(len(state.user_responses) * 5, 30)
    
    # Bonus for detecting extra red flags (10 points each, up to 20 total)
    extra_flags = [f for f in state.red_flags_detected if f not in required_flags]
    base_score += min(len(extra_flags) * 10, 20)
    
    return min(base_score, 100)

# ---------- Model setup ----------

MODEL_NAME = os.getenv("CYBERS_MODEL", "meta-llama/Llama-3.1-8B-Instruct")
DEFAULT_PLAYER = os.getenv("CYBERS_PLAYER", "players/mentor.json")
BITS = int(os.getenv("CYBERS_BITS", "4"))
TRUST_REMOTE = True

print(f"🛡️ Loading model: {MODEL_NAME}")
bnb = build_bnb(BITS)
tok = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=TRUST_REMOTE)
tok.padding_side = "left"
if tok.pad_token_id is None and tok.eos_token_id is not None:
    tok.pad_token = tok.eos_token

mdl = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
    trust_remote_code=TRUST_REMOTE,
    quantization_config=bnb,
).eval()

# ---------- Global state ----------

player = load_player(DEFAULT_PLAYER)
player_filename = os.path.splitext(os.path.basename(DEFAULT_PLAYER))[0]
conversation_history: List[Dict[str, str]] = []
MAX_HISTORY = 10

# Scenario state
current_scenario: Optional[Dict[str, Any]] = None
scenario_state: Optional[ScenarioState] = None
scenarios_cache: Dict[str, Dict[str, Any]] = {}

def build_system_text(p: Dict[str, Any]) -> str:
    """Construct system prompt from player dict."""
    return " ".join([
        f"You are {p.get('name','Assistant')}, {p.get('profession','')}.",
        f"Your personality: {p.get('personality','')}",
        f"Your communication style: {p.get('style','')}",
        "Keep facts accurate." if p.get("facts_guard") else "",
        p.get("instructions",""),
    ]).strip()

system_text = build_system_text(player)
asst_label = _first_word(player.get("name"))

print(f"🛡️ Initial player: {player.get('name', 'Unknown')} (from {DEFAULT_PLAYER})")

app = FastAPI(title="Cyber Safer API", version="1.0")

# ---------- Conversation management ----------

def add_to_history(role: str, content: str):
    """Add message to history and trim if needed."""
    global conversation_history
    conversation_history.append({"role": role, "content": content})
    if len(conversation_history) > MAX_HISTORY * 2:
        conversation_history = conversation_history[-(MAX_HISTORY * 2):]

def clear_history():
    """Clear conversation history."""
    global conversation_history
    conversation_history = []

# ---------- Generation ----------

async def stream_response(message: str) -> AsyncGenerator[str, None]:
    """Token streaming for chat UI with conversation history."""
    max_tokens = player.get("max_tokens", 250)
    temp = player.get("temperature", 0.7)
    top_p = player.get("top_p", 0.9)
    
    msgs = [{"role": "system", "content": system_text}]
    msgs.extend(conversation_history)
    msgs.append({"role": "user", "content": message})
    
    prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    inputs = tok([prompt], return_tensors="pt").to(mdl.device)

    streamer = TextIteratorStreamer(tok, skip_prompt=True, skip_special_tokens=True)
    
    collected_response = []
    
    def generate_and_stream():
        mdl.generate(
            **inputs,
            streamer=streamer,
            max_new_tokens=max_tokens,
            temperature=temp,
            top_p=top_p,
            do_sample=True,
            use_cache=True,
            eos_token_id=tok.eos_token_id,
            pad_token_id=tok.pad_token_id,
        )
    
    thread = threading.Thread(target=generate_and_stream, daemon=True)
    thread.start()
    
    for token in streamer:
        collected_response.append(token)
        yield token
    
    add_to_history("user", message)
    add_to_history("assistant", "".join(collected_response))

# ---------- Startup ----------

@app.on_event("startup")
async def startup_event():
    """Load scenarios on startup."""
    global scenarios_cache
    scenarios_cache = load_scenarios()
    print(f"✅ Loaded {len(scenarios_cache)} scenarios")

# ---------- API Endpoints ----------

@app.get("/api")
async def root():
    """Health check."""
    return {"status": "ok", "app": "Cyber Safer"}

@app.get("/api/scenarios")
async def list_scenarios():
    """List all available scenarios grouped by category."""
    categories = {}
    
    for scenario_id, scenario in scenarios_cache.items():
        category = scenario.get("category", "uncategorized")
        if category not in categories:
            categories[category] = []
        
        categories[category].append({
            "id": scenario_id,
            "title": scenario.get("title", "Untitled"),
            "difficulty": scenario.get("difficulty", "medium"),
            "description": scenario.get("introduction", "")[:100] + "..."
        })
    
    return {"categories": categories}

@app.get("/scenario/{scenario_id}")
async def get_scenario(scenario_id: str):
    """Get details of a specific scenario."""
    if scenario_id not in scenarios_cache:
        raise HTTPException(status_code=404, detail=f"Scenario '{scenario_id}' not found")
    
    return scenarios_cache[scenario_id]

@app.post("/scenario/{scenario_id}/start")
async def start_scenario(scenario_id: str):
    """Start a new scenario session."""
    global current_scenario, scenario_state, player, system_text, player_filename
    
    if scenario_id not in scenarios_cache:
        raise HTTPException(status_code=404, detail=f"Scenario '{scenario_id}' not found")
    
    scenario = scenarios_cache[scenario_id]
    
    # Load the adversary player for this scenario
    adversary_name = scenario.get("player")
    if not adversary_name:
        raise HTTPException(status_code=400, detail="Scenario missing player definition")
    
    adversary = load_player(adversary_name, base_dir="players")
    
    if not adversary:
        raise HTTPException(status_code=404, detail=f"Adversary player '{adversary_name}' not found")
    
    # Switch to adversary player
    player = adversary
    player_filename = adversary_name
    system_text = build_system_text(adversary)
    clear_history()
    
    # Initialize scenario state
    current_scenario = scenario
    scenario_state = ScenarioState(scenario_id=scenario_id)
    
    # Add initial message from adversary
    initial_msg = scenario.get("initial_message", "")
    if initial_msg:
        add_to_history("assistant", initial_msg)
    
    print(f"🎮 Started scenario: {scenario.get('title')}")
    
    return {
        "ok": True,
        "scenario": {
            "id": scenario_id,
            "title": scenario.get("title"),
            "introduction": scenario.get("introduction"),
            "category": scenario.get("category")
        },
        "initial_message": initial_msg,
        "adversary": player.get("name")
    }

@app.post("/chat/stream")
async def chat_stream(payload: Dict[str, str]):
    """Streamed chat endpoint - works in both normal and scenario mode."""
    message = payload.get("message", "").strip()
    if not message:
        raise HTTPException(status_code=400, detail="Empty message.")
    
    # If in scenario mode, track red flags
    if current_scenario and scenario_state:
        red_flags = current_scenario.get("red_flags", [])
        detected = detect_red_flags(message, red_flags)
        
        if detected:
            scenario_state.red_flags_detected.extend(detected)
            scenario_state.user_responses.append(message)
            print(f"🚩 Red flags detected: {detected}")
    
    return StreamingResponse(stream_response(message), media_type="text/plain")

@app.post("/scenario/complete")
async def complete_scenario():
    """Mark scenario as complete and calculate score."""
    global scenario_state, current_scenario
    
    if not current_scenario or not scenario_state:
        raise HTTPException(status_code=400, detail="No active scenario")
    
    # Calculate final score
    final_score = calculate_scenario_score(scenario_state, current_scenario)
    scenario_state.score = final_score
    scenario_state.completed = True
    
    # Determine if they passed
    success_criteria = current_scenario.get("success_criteria", [])
    met_criteria = [flag for flag in success_criteria if flag in scenario_state.red_flags_detected]
    passed = len(met_criteria) >= len(success_criteria) * 0.6  # 60% threshold
    
    result = {
        "score": final_score,
        "passed": passed,
        "red_flags_detected": list(set(scenario_state.red_flags_detected)),
        "red_flags_total": len(current_scenario.get("red_flags", [])),
        "success_criteria_met": met_criteria,
        "success_criteria_total": success_criteria,
        "feedback": current_scenario.get("debrief", "Well done!"),
        "learning_objectives": current_scenario.get("learning_objectives", [])
    }
    
    print(f"🏁 Scenario completed. Score: {final_score}/100, Passed: {passed}")
    
    return result

@app.post("/scenario/exit")
async def exit_scenario():
    """Exit current scenario and return to normal mode."""
    global current_scenario, scenario_state, player, system_text, player_filename
    
    # Reset to default player
    default_player = load_player(DEFAULT_PLAYER)
    player = default_player
    player_filename = os.path.splitext(os.path.basename(DEFAULT_PLAYER))[0]
    system_text = build_system_text(default_player)
    clear_history()
    
    current_scenario = None
    scenario_state = None
    
    print("👋 Exited scenario mode")
    
    return {"ok": True, "message": "Exited scenario mode"}

# ---------- Serve static UI ----------
app.mount("/", StaticFiles(directory="static", html=True), name="static")
