# 🔧 URGENT FIX: GPU Detected But Not Used

## Your Specific Problem

From your screenshots:
1. ✅ `check_gpu.py` shows: "Device: CUDA (GPU)" 
2. ✅ GPU detected: "NVIDIA GeForce RTX 5060 Ti"
3. ❌ **BUT** GPU usage still only 2%, CPU at 64%

**This means PyTorch sees the GPU but the model isn't using it!**

## What Was Wrong

The issue: `device_map="auto"` with quantized models sometimes decides to keep layers on CPU even though GPU is available. This is a known issue with bitsandbytes + "auto" device mapping.

## What I Fixed

### In cybers.py:

**1. Force CUDA device mapping:**
```python
# OLD:
device_map="auto"  # Too smart for its own good!

# NEW:
device_map_setting = "cuda" if torch.cuda.is_available() else "auto"
device_map=device_map_setting  # Explicitly force CUDA
```

**2. Explicit input device placement:**
```python
# OLD:
inputs = tok([prompt], return_tensors="pt").to(mdl.device)

# NEW:
device = next(mdl.parameters()).device
inputs = tok([prompt], return_tensors="pt")
inputs = {k: v.to(device) for k, v in inputs.items()}  # Move each tensor
```

**3. Added diagnostic output:**
Now shows:
```
✅ Model is on: cuda:0
📍 Inputs on device: cuda:0
```

## How to Apply the Fix

### Option 1: Use the Updated File (Easiest)

The fixed `cybers.py` is already in your `/mnt/user-data/outputs/` directory:

```bash
# Replace your current cybers.py with the fixed one
cp /path/to/outputs/cybers.py ./cybers.py
```

### Option 2: Manual Changes

If you want to patch your existing file, make these 3 changes:

1. Around line 164, change:
   ```python
   device_map="auto"
   ```
   to:
   ```python
   device_map="cuda" if torch.cuda.is_available() else "auto"
   ```

2. Around line 226, change:
   ```python
   inputs = tok([prompt], return_tensors="pt").to(mdl.device)
   ```
   to:
   ```python
   device = next(mdl.parameters()).device
   inputs = tok([prompt], return_tensors="pt")
   inputs = {k: v.to(device) for k, v in inputs.items()}
   ```

3. Add diagnostic output after model loading to verify device.

## Test It Works

### Step 1: Start the server
```bash
./start.sh
```

### Step 2: Check startup output
**MUST see:**
```
✅ Model is on: cuda:0  ← CRITICAL! Must say cuda, not cpu
```

**If it says "cpu", the fix didn't work!**

### Step 3: Test generation
Send a chat message and watch `nvidia-smi`:

```bash
# In another terminal:
watch -n 1 nvidia-smi
```

**MUST see:**
- GPU-Util: 85-100% (not 2%!)
- Memory-Usage: 4-6GB (not ~0.5GB)

### Step 4: Check performance
- Token rate should be 15-30/sec (not 1-3/sec)
- Response time should be 3-10sec (not 30-60sec)

## If Still Not Working

### Try 8-bit quantization instead of 4-bit:
```bash
# In config.env:
export CYBERS_BITS=8
```

### Or try no quantization:
```bash
export CYBERS_BITS=""
```

### Nuclear option - edit cybers.py line ~164:
```python
device_map={"": 0}  # Force EVERYTHING to GPU 0
```

## Expected Results

| Metric | Before | After Fix |
|--------|--------|-----------|
| Model Device | "cuda:0" but not used | "cuda:0" AND used ✅ |
| GPU Usage | 2% | 85-100% ✅ |
| VRAM | ~0.5GB | 4-6GB ✅ |
| Speed | 1-3 tok/sec | 15-30 tok/sec ✅ |
| Response | 30-60sec | 3-10sec ✅ |

## Why This Happens

`device_map="auto"` tries to automatically split model across devices. With bitsandbytes quantization:
1. Model layers are quantized to save memory
2. "auto" miscalculates available VRAM
3. Decides to put some layers on CPU "just to be safe"
4. This creates CPU bottleneck
5. Entire generation becomes CPU-bound

**Solution:** Don't use "auto" - explicitly tell it to use CUDA.

## Verification Checklist

After the fix, verify:
- [ ] Startup shows "Model is on: cuda:0"
- [ ] During generation shows "Inputs on device: cuda:0"
- [ ] `nvidia-smi` shows 85-100% GPU usage
- [ ] `nvidia-smi` shows 4-6GB VRAM usage
- [ ] Generation is 15-30 tokens/sec
- [ ] Responses come in 3-10 seconds

If ANY of these fail, GPU is still not being used properly!

## More Help

See `docs/GPU_DEVICE_MAP_FIX.md` for:
- Detailed explanation
- Alternative solutions
- Debug scripts
- Advanced troubleshooting

The fixed `cybers.py` is ready to use - just copy it over and restart! 🚀
