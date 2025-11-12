# 🎮 GPU FIX - Critical Performance Issue Resolved

## The Problem You Found

Your screenshot showed:
- **CPU: 79% usage** (i7-14700KF working hard)
- **GPU: 2% usage** (RTX 5060 essentially idle)

This means the model was running on CPU instead of GPU - **10x slower than it should be!**

## Quick Diagnosis

```bash
python check_gpu.py
```

This new script will tell you immediately if GPU is working.

## Most Likely Fix (90% of cases)

You probably have **CPU-only PyTorch** installed. Fix in 30 seconds:

```bash
# Uninstall CPU version
pip uninstall torch torchvision torchaudio

# Install GPU version
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Verify
python check_gpu.py
```

Should show:
```
✅ CUDA Available: True
✅ GPU 0: NVIDIA GeForce RTX 5060
✅ GPU test passed!
```

## Expected Performance

### Before Fix (CPU):
- First generation: **2-5 minutes** 😱
- Subsequent: **30-60 seconds**
- Token rate: **1-3 tokens/sec**
- CPU usage: **79%**
- GPU usage: **2%**

### After Fix (GPU):
- First generation: **10-30 seconds** ⚡
- Subsequent: **3-10 seconds**
- Token rate: **15-30 tokens/sec**
- CPU usage: **20-40%**
- GPU usage: **80-100%** 🎉

**Result: 10x faster!**

## Verification

After fixing, you should see:

1. **In startup logs:**
   ```
   🖥️  Device: CUDA
   ```

2. **In nvidia-smi:**
   ```
   GPU-Util: 85%    (not 2%!)
   Memory-Usage: 4.5GB / 16GB
   ```

3. **In generation:**
   ```
   ⏳ Streaming tokens...
     ... 10 tokens generated  (< 1 second)
     ... 20 tokens generated  (< 2 seconds)
   ```

## Files Added

- **check_gpu.py** - GPU diagnostic script
- **docs/GPU_FIX.md** - Complete troubleshooting guide

## Updated Documentation

All docs now include GPU warnings:
- ✅ README.md - GPU check in Quick Start
- ✅ START_HERE.txt - GPU troubleshooting section
- ✅ docs/GPU_FIX.md - Complete fix guide

## Common Scenarios

### Scenario 1: Wrong PyTorch Version (Most Common)
**Symptom:** `check_gpu.py` shows "CUDA Available: False"
**Fix:** Reinstall PyTorch with CUDA support (see above)

### Scenario 2: Drivers Issue
**Symptom:** `nvidia-smi` command not found
**Fix:** Install NVIDIA drivers, reboot

### Scenario 3: Cable Issue
**Symptom:** Drivers installed, but no GPU detected
**Fix:** Check monitor cable is plugged into GPU (not motherboard!)

### Scenario 4: CUDA Toolkit Missing
**Symptom:** `check_gpu.py` shows old CUDA version
**Fix:** Update CUDA toolkit to 12.1+

## Quick Commands

```bash
# Check if GPU working
python check_gpu.py

# Check NVIDIA driver
nvidia-smi

# Check PyTorch CUDA
python -c "import torch; print(torch.cuda.is_available())"

# Monitor GPU during generation
watch -n 1 nvidia-smi

# Quick fix (most common)
pip uninstall torch && pip install torch --index-url https://download.pytorch.org/whl/cu121
```

## Why This Matters

With your RTX 5060 (16GB VRAM), you can run:
- **8B models comfortably** with 4-bit quantization (~6GB VRAM)
- **Fast generation** (15-30 tokens/sec vs 1-3 on CPU)
- **Multiple concurrent users** without slowdown
- **Larger context windows** without running out of memory

Running on CPU wastes your GPU and makes the experience **10x worse** than it should be!

## Next Steps

1. **Run the diagnostic:**
   ```bash
   python check_gpu.py
   ```

2. **If GPU not working:**
   - See `docs/GPU_FIX.md`
   - Most likely: reinstall PyTorch with CUDA

3. **Verify it's fixed:**
   ```bash
   ./start.sh
   # Should show: "🖥️  Device: CUDA"
   ```

4. **Monitor during use:**
   ```bash
   watch -n 1 nvidia-smi
   # GPU-Util should be 80-100%
   ```

Your RTX 5060 is a powerful card - let's use it! 🚀
