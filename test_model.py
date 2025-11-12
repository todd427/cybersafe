#!/usr/bin/env python3
"""
Quick test script to verify the LLM is loaded and working.

Run this before starting the full server to catch any issues early.
"""

import os
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

def test_model():
    """Test model loading and basic generation."""
    
    MODEL_NAME = os.getenv("CYBERS_MODEL", "meta-llama/Llama-3.1-8B-Instruct")
    BITS = int(os.getenv("CYBERS_BITS", "4"))
    
    print("=" * 60)
    print("🛡️  CYBER SAFER - MODEL TEST")
    print("=" * 60)
    print(f"\n📦 Model: {MODEL_NAME}")
    print(f"🔧 Quantization: {BITS}-bit")
    print(f"🖥️  Device: {'CUDA (GPU)' if torch.cuda.is_available() else 'CPU'}")
    
    if torch.cuda.is_available():
        print(f"🎮 GPU: {torch.cuda.get_device_name(0)}")
        print(f"💾 GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
    
    print("\n" + "=" * 60)
    print("⏳ LOADING MODEL (this may take 1-2 minutes)...")
    print("=" * 60)
    
    try:
        # Build quantization config
        bnb = None
        if BITS == 4:
            bnb = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
            )
        elif BITS == 8:
            bnb = BitsAndBytesConfig(load_in_8bit=True)
        
        # Load tokenizer
        print("\n1️⃣  Loading tokenizer...")
        tok = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
        tok.padding_side = "left"
        if tok.pad_token_id is None and tok.eos_token_id is not None:
            tok.pad_token = tok.eos_token
        print("   ✅ Tokenizer loaded")
        
        # Load model
        print("\n2️⃣  Loading model (largest step, please wait)...")
        mdl = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            device_map="auto",
            dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
            trust_remote_code=True,
            quantization_config=bnb,
            offload_buffers=True,
        ).eval()
        print("   ✅ Model loaded")
        
        # Calculate model size
        param_count = sum(p.numel() for p in mdl.parameters()) / 1e9
        print(f"\n📊 Model has {param_count:.2f}B parameters")
        
        print("\n" + "=" * 60)
        print("3️⃣  TESTING GENERATION")
        print("=" * 60)
        
        # Test generation
        test_message = "Say 'Hello! The model is working!' and nothing else."
        print(f"\n💬 Test prompt: {test_message}")
        
        msgs = [{"role": "user", "content": test_message}]
        prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
        inputs = tok([prompt], return_tensors="pt").to(mdl.device)
        
        print("🚀 Generating response...")
        
        with torch.no_grad():
            outputs = mdl.generate(
                **inputs,
                max_new_tokens=50,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tok.pad_token_id,
            )
        
        response = tok.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
        
        print(f"\n🤖 Model response: {response.strip()}")
        
        print("\n" + "=" * 60)
        print("✅ SUCCESS! Model is working correctly.")
        print("=" * 60)
        print("\n💡 You can now start the server with:")
        print("   uvicorn cybers:app --reload --port 8021")
        print("\n")
        
        return True
        
    except Exception as e:
        print("\n" + "=" * 60)
        print("❌ ERROR: Model test failed")
        print("=" * 60)
        print(f"\n⚠️  {type(e).__name__}: {str(e)}")
        print("\n💡 Troubleshooting:")
        print("   - Check if you have enough RAM/VRAM")
        print("   - Try a smaller model or higher quantization")
        print("   - Ensure transformers library is up to date")
        print("   - Check if model name is correct")
        print("\n")
        return False

if __name__ == "__main__":
    success = test_model()
    sys.exit(0 if success else 1)
