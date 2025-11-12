# 🎮 GPU Not Being Used - Fix Guide

## Problem

Your RTX 5060 shows only 2% usage while CPU is at 79%. The model is running on CPU instead of GPU, which is **much slower**.

## Quick Diagnosis

Run this first:

```bash
python check_gpu.py
```

This will tell you exactly what's wrong.

## Most Likely Cause

You probably have the **CPU-only version of PyTorch** installed. This is a common issue!

## Solution 1: Reinstall PyTorch with CUDA Support

### Step 1: Uninstall current PyTorch
```bash
pip uninstall torch torchvision torchaudio
```

### Step 2: Install GPU version
For CUDA 12.1 (recommended for RTX 5060):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

For CUDA 11.8 (if 12.1 doesn't work):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Step 3: Verify it works
```bash
python check_gpu.py
```

You should see:
```
✅ CUDA Available: True
✅ GPU 0: NVIDIA GeForce RTX 5060
✅ GPU test passed!
```

### Step 4: Test with your model
```bash
python test_model.py
```

Now you should see:
```
🖥️  Device: CUDA
```

## Solution 2: Check NVIDIA Drivers

### Verify drivers are installed:
```bash
nvidia-smi
```

You should see your RTX 5060 listed. If not:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install nvidia-driver-545  # or latest version
sudo reboot
```

**Fedora/RHEL:**
```bash
sudo dnf install akmod-nvidia
sudo reboot
```

After reboot, run `nvidia-smi` again.

## Solution 3: Force CUDA Usage

If PyTorch sees CUDA but cybers.py still uses CPU, you can force it:

Edit `cybers.py` and change line ~167 from:
```python
device_map="auto",
```

To:
```python
device_map="cuda:0",  # Force GPU 0
```

## Verification

After fixing, verify GPU is being used:

### 1. Run the diagnostic:
```bash
python check_gpu.py
```

Should show:
- ✅ CUDA Available: True
- ✅ GPU test passed

### 2. Start the server:
```bash
./start.sh
```

Should show:
```
🖥️  Device: CUDA
```

### 3. Monitor GPU usage:
In another terminal:
```bash
watch -n 1 nvidia-smi
```

During generation, you should see:
- **GPU Util: 80-100%** (not 2%!)
- **Memory Used: 4-6GB** (not near 0)

### 4. Performance check:

**Before (CPU):**
- First generation: 2-5 minutes
- Subsequent: 30-60 seconds
- Token rate: 1-3 tokens/sec

**After (GPU):**
- First generation: 10-30 seconds
- Subsequent: 3-10 seconds
- Token rate: 15-30 tokens/sec

If you see **10x speedup**, GPU is working! 🎉

## Common Issues

### Issue: "CUDA out of memory"

**Solution:** Use smaller model or more quantization:
```bash
# In config.env:
export CYBERS_MODEL="meta-llama/Llama-3.2-3B-Instruct"
export CYBERS_BITS="4"
```

### Issue: "No CUDA-capable device detected"

**Solutions:**
1. Check cable is connected to GPU (not motherboard!)
2. Enable GPU in BIOS
3. Reseat GPU
4. Update NVIDIA drivers

### Issue: "CUDA driver version insufficient"

**Solution:** Update NVIDIA drivers:
```bash
# Check current version
nvidia-smi

# Update drivers (Ubuntu)
sudo apt update
sudo apt upgrade nvidia-driver-*
sudo reboot
```

### Issue: Multiple GPUs, wrong one selected

**Solution:** Specify GPU in config.env:
```bash
export CUDA_VISIBLE_DEVICES=0  # Use first GPU
```

## Expected Performance

With RTX 5060 (16GB VRAM):

| Model | GPU Usage | VRAM | Speed |
|-------|-----------|------|-------|
| Llama-3.2-1B (4-bit) | 60-80% | ~2GB | 30+ tok/s |
| Llama-3.2-3B (4-bit) | 70-90% | ~4GB | 25+ tok/s |
| Llama-3.1-8B (4-bit) | 80-100% | ~6GB | 15-20 tok/s |
| Llama-3.1-8B (8-bit) | 80-100% | ~10GB | 12-18 tok/s |

## Quick Test Script

Create a quick test:

```python
import torch
print(f"CUDA: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    x = torch.randn(1000, 1000).cuda()
    print(f"✅ GPU working!")
```

Save as `quick_gpu_test.py` and run:
```bash
python quick_gpu_test.py
```

## Need More Help?

1. Run `python check_gpu.py` and share the output
2. Run `nvidia-smi` and share the output
3. Run `pip list | grep torch` and share the output

These will help diagnose the exact issue.

## TL;DR - Quick Fix

Most common fix (90% of cases):

```bash
# Uninstall CPU PyTorch
pip uninstall torch torchvision torchaudio

# Install GPU PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Test it
python check_gpu.py

# If working, restart
./start.sh
```

Your GPU usage should now be 80-100% during generation! 🚀
