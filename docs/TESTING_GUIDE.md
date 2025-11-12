# Cyber Safer - Testing & Debugging Guide

## Overview

This updated version includes:
- ✅ Fixed deprecated `torch_dtype` → `dtype` 
- ✅ Added `offload_buffers=True` to prevent OOM warnings
- ✅ Enhanced debugging output during model loading and generation
- ✅ Test scripts to verify everything works before running the server

## Quick Start Testing

### Step 1: Test Model Loading (Offline)

Before starting the server, test if the model loads correctly:

```bash
python test_model.py
```

This will:
- Show detailed loading progress
- Test basic model generation
- Display system information (GPU/CPU, memory)
- Take 1-2 minutes for the initial load

**Expected output:**
```
🛡️  CYBER SAFER - MODEL TEST
📦 Model: meta-llama/Llama-3.1-8B-Instruct
🔧 Quantization: 4-bit
🖥️  Device: CUDA (GPU)
⏳ LOADING MODEL (this may take 1-2 minutes)...
...
✅ SUCCESS! Model is working correctly.
```

### Step 2: Start the Server

Once the model test passes:

```bash
uvicorn cybers:app --reload --port 8021
```

**Watch for these signs:**
```
🛡️ Loading model: meta-llama/Llama-3.1-8B-Instruct
🔧 Quantization: 4-bit
🖥️  Device: CUDA
⏳ Loading model (this may take 1-2 minutes)...
✅ Model loaded successfully!
📊 Model size: 8.03B parameters
✅ Loaded 12 scenarios
INFO:     Uvicorn running on http://127.0.0.1:8021
```

### Step 3: Test the Running Server

In a new terminal:

```bash
# Test health endpoint
python test_client.py

# Test model generation
python test_client.py test

# Test chat
python test_client.py chat "Hello!"

# Test scenarios
python test_client.py scenarios
```

## Debugging Tips

### If Model Loading Hangs

**Signs:**
- No output after "⏳ Loading model..."
- Process sits at 100% CPU for >5 minutes
- No GPU activity (if using GPU)

**Solutions:**
1. Check available RAM: Model needs ~8GB for 4-bit quantization
2. Try smaller model: `export CYBERS_MODEL="meta-llama/Llama-3.2-3B-Instruct"`
3. Try 8-bit instead: `export CYBERS_BITS=8`
4. Check GPU memory: `nvidia-smi` (if using GPU)

### If Generation is Slow

**Normal speeds:**
- First generation: 10-30 seconds (model warming up)
- Subsequent generations: 3-10 seconds
- Token rate: ~5-20 tokens/second (varies by hardware)

**If slower:**
- Check CPU/GPU usage
- Verify model is on GPU: Look for "Device: CUDA" in logs
- Try reducing `max_tokens` in player JSON files

### Monitoring Real-Time Activity

The enhanced logging shows:
```
💬 User message: hello...
🎯 Generating with max_tokens=250, temp=0.7, top_p=0.9
🚀 Starting generation thread...
⏳ Streaming tokens...
  ... 10 tokens generated
  ... 20 tokens generated
✓ Generation thread completed
✅ Response complete: 156 chars, 23 tokens
```

If you don't see these messages, generation might be stuck.

## Test Endpoints

The server now includes a test endpoint:

```bash
curl http://localhost:8021/api/test
```

Returns:
```json
{
  "status": "success",
  "model": "meta-llama/Llama-3.1-8B-Instruct",
  "device": "cuda:0",
  "response": "Model is working!",
  "message": "Model is working correctly!"
}
```

## Environment Variables

```bash
# Use a different model
export CYBERS_MODEL="meta-llama/Llama-3.2-3B-Instruct"

# Change quantization
export CYBERS_BITS=8  # or 4, or omit for no quantization

# Change default player
export CYBERS_PLAYER="players/mentor.json"
```

## Common Issues

### "CUDA out of memory"
- Model too large for GPU
- Solution: Use 8-bit quantization or smaller model

### "RuntimeError: probability tensor contains NaN"
- Usually happens with temperature=0
- Solution: Use temperature >= 0.1

### Server starts but doesn't respond
- Model might still be loading in background
- Wait 1-2 minutes and try test_client.py again

### Warnings are normal
Some warnings during load are expected and harmless:
- ✅ "Some weights...were not initialized" - normal for quantized models
- ✅ "Using pad_token" - handled automatically
- ❌ "CUDA out of memory" - NOT normal, reduce model size

## Success Checklist

- [ ] `test_model.py` completes successfully
- [ ] Server starts and shows "✅ Model loaded successfully!"
- [ ] `test_client.py` returns OK
- [ ] `test_client.py test` generates a response
- [ ] `test_client.py chat` has a conversation
- [ ] Web UI loads at http://localhost:8021

## Getting Help

If tests fail:
1. Check `test_model.py` output for specific error
2. Verify system has enough RAM (8GB+ recommended)
3. Check transformers version: `pip show transformers`
4. Try a smaller model first
5. Check GPU with: `nvidia-smi` (if applicable)

Good luck! 🛡️
