# 🚀 Getting Started with Cyber Safer

## Overview

Cyber Safer is an AI-powered cybersecurity training platform. This guide will get you up and running in minutes.

## Prerequisites

- Python 3.8+
- 8GB+ RAM (or 4GB with small model)
- Optional: NVIDIA GPU with CUDA support

## Installation

1. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn torch transformers accelerate bitsandbytes
   ```

2. **Get the files:**
   - Extract all files to a directory
   - Create `players/` and `scenarios/` directories (if not included)

## First-Time Setup

### Step 1: Configure (Optional but Recommended)

```bash
# Copy the configuration template
cp config.env.example config.env

# Edit to customize (optional)
nano config.env
```

**Default settings work for most systems!** Only edit if you need to:
- Use a smaller/larger model
- Change port or host
- Adjust memory settings

### Step 2: Test the Model

**This is important!** Test before starting the full server:

```bash
python test_model.py
```

Expected output:
```
🛡️  CYBER SAFER - MODEL TEST
📦 Model: meta-llama/Llama-3.1-8B-Instruct
🔧 Quantization: 4-bit
🖥️  Device: CUDA (GPU)
⏳ LOADING MODEL (this may take 1-2 minutes)...
✅ Model loaded successfully!
🤖 Model response: Hello! The model is working!
✅ SUCCESS!
```

If this fails, see [Troubleshooting](#troubleshooting) below.

### Step 3: Start the Server

```bash
./start.sh
```

This will:
1. Load your config.env (if it exists)
2. Test the model again
3. Start the server

You'll see:
```
📋 Active Configuration:
   Model: meta-llama/Llama-3.1-8B-Instruct
   Quantization: 4-bit
   Player: players/mentor.json
   Server: http://127.0.0.1:8021

✅ Model test passed!
💡 Open http://127.0.0.1:8021 in your browser
```

### Step 4: Test the Server

In a **new terminal:**

```bash
# Quick health check
python test_client.py

# Full test with model generation
python test_client.py test

# Test chat
python test_client.py chat "Hello!"
```

### Step 5: Use the Web Interface

Open your browser to: **http://localhost:8021**

You should see the Cyber Safer web interface!

## Quick Reference Commands

```bash
# Test model (offline)
python test_model.py

# Start server (with config)
./start.sh

# Test server (in new terminal)
python test_client.py test

# Chat test
python test_client.py chat "Hi there!"

# Test scenarios
python test_client.py scenarios

# Manual start (without start.sh)
uvicorn cybers:app --reload --port 8021
```

## Configuration Examples

### For Low-End Systems

Edit `config.env`:
```bash
export CYBERS_MODEL="meta-llama/Llama-3.2-1B-Instruct"
export CYBERS_BITS="4"
```

### For Network Access

Edit `config.env`:
```bash
export CYBERS_HOST="0.0.0.0"  # Allow external connections
export CYBERS_PORT="8080"     # Custom port
```

### For Best Quality

Edit `config.env`:
```bash
export CYBERS_MODEL="meta-llama/Llama-3.1-8B-Instruct"
export CYBERS_BITS="8"  # Less compression
```

## Troubleshooting

### Model Won't Load

**Error: Out of memory**
```bash
# Solution 1: Use smaller model
export CYBERS_MODEL="meta-llama/Llama-3.2-3B-Instruct"

# Solution 2: Increase quantization
export CYBERS_BITS=8
```

**Error: Can't download model**
- Check internet connection
- Verify HuggingFace is accessible
- Try: `export HF_HOME=/path/to/cache`

### Server Won't Start

**Error: Port already in use**
```bash
# Find what's using the port
lsof -i :8021

# Use a different port
export CYBERS_PORT=8022
```

**Error: Module not found**
```bash
# Install missing dependencies
pip install fastapi uvicorn torch transformers accelerate bitsandbytes
```

### Slow Generation

**First generation is slow (10-30 seconds)**
- This is normal! The model is warming up
- Subsequent generations will be faster (3-10 seconds)

**All generations are slow**
- Check CPU/GPU usage
- Verify model is on GPU: Look for "Device: CUDA"
- Try smaller model
- Check if system is swapping (not enough RAM)

### Can't Connect to Web Interface

1. **Check server is running:**
   ```bash
   curl http://localhost:8021/api
   ```

2. **Check for errors in server output**

3. **Try different browser**

4. **Check firewall settings**

## Understanding the Output

### During Startup
```
🛡️ Loading model: meta-llama/Llama-3.1-8B-Instruct
🔧 Quantization: 4-bit
🖥️  Device: CUDA
⏳ Loading model (this may take 1-2 minutes)...
✅ Model loaded successfully!
📊 Model size: 8.03B parameters
```

### During Chat
```
💬 User message: hello...
🎯 Generating with max_tokens=250, temp=0.7
🚀 Starting generation thread...
⏳ Streaming tokens...
  ... 10 tokens generated
  ... 20 tokens generated
✅ Response complete: 156 chars, 23 tokens
```

These messages help you understand what's happening and diagnose issues!

## Next Steps

Once everything is working:

1. **Explore the web interface** at http://localhost:8021
2. **Try different scenarios** from the categories
3. **Read the documentation:**
   - `CONFIG_GUIDE.md` - Detailed configuration
   - `TESTING_GUIDE.md` - Testing and debugging
   - `QUICK_REFERENCE.txt` - Command reference

4. **Customize:**
   - Add your own scenarios in `scenarios/`
   - Create custom AI personas in `players/`
   - Adjust settings in `config.env`

## Support

If you're stuck:

1. Run `python test_model.py` to see exact error
2. Check the troubleshooting sections above
3. Review `TESTING_GUIDE.md` for detailed help
4. Check system resources (RAM, disk space)
5. Try a smaller model configuration

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 4GB | 8GB+ |
| Storage | 5GB | 10GB+ (for cache) |
| CPU | Any modern CPU | Multi-core |
| GPU | None (can use CPU) | NVIDIA with CUDA |

## File Structure

```
cyber-safer/
├── cybers.py              # Main application
├── start.sh               # Smart launcher
├── config.env.example     # Config template
├── config.env             # Your config (create this)
├── test_model.py          # Model tester
├── test_client.py         # Server tester
├── players/               # AI personas
│   ├── mentor.json
│   ├── phishing_emailer.json
│   └── ...
├── scenarios/             # Training scenarios
│   ├── phishing_bank.json
│   └── ...
└── static/                # Web interface files
    ├── index.html
    ├── css/
    └── js/
```

## Success Checklist

- [ ] Dependencies installed
- [ ] `test_model.py` completes successfully
- [ ] No warnings during startup
- [ ] Server shows "✅ Model loaded successfully!"
- [ ] `/api/test` endpoint returns success
- [ ] `test_client.py test` passes
- [ ] Web UI loads at http://localhost:8021
- [ ] Can chat with the AI
- [ ] Can load scenarios

**All checked?** You're ready to train! 🎉

## Quick Commands Summary

```bash
# Setup (first time)
cp config.env.example config.env
nano config.env

# Test and start
python test_model.py    # Test first
./start.sh              # Start server

# In new terminal
python test_client.py test

# Open browser
open http://localhost:8021
```

Happy cyber safety training! 🛡️

---

**Need more help?**
- Detailed testing: `TESTING_GUIDE.md`
- Configuration: `CONFIG_GUIDE.md`
- Quick reference: `QUICK_REFERENCE.txt`
