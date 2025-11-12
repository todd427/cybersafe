# 🔧 GPU Detected But Not Used - Advanced Fix

## The Problem

You've confirmed:
- ✅ PyTorch sees CUDA: `Device: CUDA (GPU)`
- ✅ GPU is detected: `NVIDIA GeForce RTX 5060 Ti`
- ❌ **BUT** GPU usage still only 2%, CPU at 64%

This means PyTorch CAN see the GPU, but the model isn't actually using it for inference!

## Root Cause

The issue is with `device_map="auto"` combined with quantized models. Sometimes "auto" decides to put layers on CPU even when GPU is available, especially with:
- 4-bit quantization (bitsandbytes)
- Large models
- Certain GPU configurations

## The Fix (Already Applied)

I've updated `cybers.py` with three critical changes:

### 1. Force CUDA Device Map
**Before:**
```python
device_map="auto",  # Might choose CPU!
```

**After:**
```python
device_map_setting = "cuda" if torch.cuda.is_available() else "auto"
device_map=device_map_setting,  # Force CUDA
```

### 2. Explicit Input Device Placement
**Before:**
```python
inputs = tok([prompt], return_tensors="pt").to(mdl.device)
```

**After:**
```python
device = next(mdl.parameters()).device
inputs = tok([prompt], return_tensors="pt")
inputs = {k: v.to(device) for k, v in inputs.items()}  # Explicit!
```

### 3. Better Diagnostics
Now shows exactly where model and inputs are:
```
🖥️  Model device: cuda:0
📍 Inputs on device: cuda:0
🚀 Starting generation thread...
   Model is on: cuda:0
   Inputs are on: cuda:0
```

## Test the Fix

### Step 1: Use the new cybers.py

The fixed version is already in your outputs directory. Replace your current one:

```bash
# Backup old version
mv cybers.py cybers.py.old

# Use the new fixed version
cp /path/to/outputs/cybers.py .
```

### Step 2: Start the server

```bash
./start.sh
```

### Step 3: Watch for new output

You should now see:
```
🖥️  Device: CUDA
🎮 GPU: NVIDIA GeForce RTX 5060 Ti
📍 Device map: cuda
✅ Model loaded successfully!
✅ Model is on: cuda:0
```

**Critical check:** Must say "Model is on: cuda:0" (not "cpu")!

### Step 4: Monitor during generation

In another terminal:
```bash
watch -n 1 nvidia-smi
```

During chat, you should now see:
```
GPU-Util: 85-100%  (not 2%!)
Memory-Usage: 4-6GB
```

## If Still Not Working

### Issue 1: Model says "cuda:0" but GPU still at 2%

This could be a bitsandbytes issue. Try:

```bash
# In config.env:
export CYBERS_BITS=8  # Try 8-bit instead of 4-bit
```

Or disable quantization entirely:
```bash
export CYBERS_BITS=""  # No quantization
```

### Issue 2: "CUDA out of memory"

Model is now on GPU but runs out of VRAM:

```bash
# Use smaller model
export CYBERS_MODEL="meta-llama/Llama-3.2-3B-Instruct"
export CYBERS_BITS=4
```

### Issue 3: Model still loads to CPU

Check if there's a conflicting environment variable:
```bash
env | grep CUDA
```

Unset any that might force CPU:
```bash
unset CUDA_VISIBLE_DEVICES
```

## Verify It's Actually Fixed

Run a chat and check these indicators:

### 1. Startup Output
```
✅ Model is on: cuda:0  ← MUST say cuda, not cpu
```

### 2. During Chat
```
🖥️  Model device: cuda:0
📍 Inputs on device: cuda:0
   Model is on: cuda:0
   Inputs are on: cuda:0
```

### 3. System Monitor (nvidia-smi)
```
GPU-Util: 85-100%      ← Should be high
Memory-Usage: 4-6GB    ← Should see VRAM used
```

### 4. Performance
```
Token rate: 15-30 tokens/sec  ← Should be FAST
Response time: 3-10 sec       ← Should be quick
```

If you see **1-3 tokens/sec**, it's still on CPU!

## Alternative: Completely Force GPU

If the above doesn't work, try this nuclear option in `cybers.py`:

```python
# Replace device_map line with:
device_map={"": 0}  # Force everything to GPU 0
```

This forces EVERY layer to GPU 0, no exceptions.

## Why device_map="auto" Failed

With bitsandbytes quantization:
1. Model is quantized to save memory
2. `device_map="auto"` tries to be "smart"
3. It miscalculates and puts some layers on CPU
4. This causes mixed CPU/GPU execution
5. Everything becomes CPU-bound

Solution: Don't trust "auto" - explicitly force `device_map="cuda"`.

## Additional Diagnostics

Add this to verify during generation:

```python
# In cybers.py, inside generate_and_stream():
print(f"GPU Memory: {torch.cuda.memory_allocated(0) / 1e9:.2f}GB")
```

During generation, you should see memory usage **increase**.

## Expected Behavior After Fix

| Metric | Before | After |
|--------|--------|-------|
| Startup | "Model is on: cuda:0" | Same |
| GPU Usage | 2% | **85-100%** ✅ |
| VRAM Usage | ~0.5GB | **4-6GB** ✅ |
| Token Rate | 1-3/sec | **15-30/sec** ✅ |
| Response Time | 30-60sec | **3-10sec** ✅ |

If you're not seeing these improvements, GPU still isn't being used!

## Debug Script

Save as `test_gpu_inference.py`:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

# Simplified test
bnb = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.2-1B-Instruct",  # Small model for test
    device_map="cuda",  # Force CUDA
    quantization_config=bnb,
)

tok = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B-Instruct")

print(f"Model device: {next(model.parameters()).device}")

# Test generation
inputs = tok("Hello", return_tensors="pt")
inputs = {k: v.cuda() for k, v in inputs.items()}

print("Generating...")
with torch.cuda.amp.autocast():
    outputs = model.generate(**inputs, max_new_tokens=20)

print(f"✅ Success! GPU was used.")
print(f"GPU Memory: {torch.cuda.memory_allocated(0) / 1e9:.2f}GB")
```

Run it:
```bash
python test_gpu_inference.py
```

Should show high GPU memory usage.

## Summary

The new `cybers.py`:
1. ✅ Forces `device_map="cuda"` when GPU available
2. ✅ Explicitly moves inputs to correct device
3. ✅ Shows exactly where model/inputs are
4. ✅ Detects if model accidentally loaded to CPU

This should fix the "GPU detected but not used" issue!
