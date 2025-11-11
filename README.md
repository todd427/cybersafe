I’ve got plenty to work with from `cybers.py` — it’s a full FastAPI app for interactive, AI-driven cybersecurity training. Here’s a suitable **README.md** for your repo:

---

````markdown
# 🛡️ Cyber Safer

**Interactive cybersecurity training through AI-powered scenarios.**  
Cyber Safer lets users practice identifying scams, phishing attempts, and social-engineering traps in safe, conversational simulations powered by local or remote LLMs.

---

## 🚀 Quick Start

### 1. Install dependencies
Create a virtual environment and install required packages:
```bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn torch transformers accelerate bitsandbytes
````

### 2. Prepare content

The app expects two directories:

```
players/     → AI persona definitions (JSON)
scenarios/   → Training scenarios (JSON)
```

Example:

```
players/
  mentor.json
  scammer.json
scenarios/
  phishing_bank.json
  romance_scam.json
```

### 3. Run the server

```bash
uvicorn cybers:app --reload --port 8021
```

Then open your browser at:
👉 [http://localhost:8021](http://localhost:8021)

---

## 🧠 How It Works

1. **Model loading** – by default uses `meta-llama/Llama-3.1-8B-Instruct` (configurable).
2. **Players** – JSON “personas” define tone, profession, and behaviour (e.g. *mentor*, *attacker*).
3. **Scenarios** – each JSON file describes a phishing or scam situation, its *red-flags*, *success criteria*, and *debrief*.
4. **Interactive chat** – the user converses with the AI adversary; `detect_red_flags()` spots awareness cues in their replies.
5. **Scoring** – red-flag recognition, message quality, and safe behaviour yield up to 100 points.
6. **Completion** – `/scenario/complete` returns score, feedback, and learning objectives.

---

## ⚙️ Environment Variables

| Variable        | Purpose                      | Default                            |
| --------------- | ---------------------------- | ---------------------------------- |
| `CYBERS_MODEL`  | Hugging Face model name/path | `meta-llama/Llama-3.1-8B-Instruct` |
| `CYBERS_PLAYER` | Default mentor JSON          | `players/mentor.json`              |
| `CYBERS_BITS`   | Quantization (4 or 8)        | `4`                                |

Example:

```bash
export CYBERS_MODEL="Qwen/Qwen2.5-7B-Instruct"
export CYBERS_BITS=4
```

---

## 🧩 API Endpoints

| Method   | Path                   | Description                    |
| :------- | :--------------------- | :----------------------------- |
| **GET**  | `/api`                 | Health check                   |
| **GET**  | `/api/scenarios`       | List all scenarios by category |
| **GET**  | `/scenario/{id}`       | Get scenario details           |
| **POST** | `/scenario/{id}/start` | Start a scenario session       |
| **POST** | `/chat/stream`         | Stream chat responses          |
| **POST** | `/scenario/complete`   | Finish and score a scenario    |
| **POST** | `/scenario/exit`       | Exit back to default mode      |

Static front-end files are served from `static/`.

---

## 🧱 Project Structure

```
cybers.py          ← FastAPI app
players/           ← Persona JSONs
scenarios/         ← Scenario JSONs
static/            ← Optional web UI
README.md
requirements.txt   ← (generate with pip freeze)
```

---

## 💡 Extending Cyber Safer

* Add new **players** to vary tone and difficulty.
* Add **scenarios** for spear-phishing, romance scams, fake tech support, etc.
* Replace or fine-tune the **LLM** with any compatible model on Hugging Face.
* Integrate with a web dashboard for multi-user analytics or classroom use.

---

## 🧾 License

MIT License © 2025 Foxxe Labs / Todd McCaffrey
Educational use encouraged — teach security through conversation, not fear.

```

---

Would you like me to generate a matching `requirements.txt` and sample `players/mentor.json` + `scenarios/phishing_bank.json` to make it runnable out-of-the-box?
```

