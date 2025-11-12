#!/usr/bin/env python3
"""
GPU Diagnostic Script - Check CUDA availability and configuration
"""

import sys

print("=" * 60)
print("🔍 GPU DIAGNOSTIC")
print("=" * 60)

# Check PyTorch
try:
    import torch
    print(f"\n✅ PyTorch installed: {torch.__version__}")
except ImportError:
    print("\n❌ PyTorch not installed!")
    print("Install with: pip install torch")
    sys.exit(1)

# Check CUDA availability
print(f"\n🎮 CUDA Available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"✅ CUDA Version: {torch.version.cuda}")
    print(f"✅ cuDNN Version: {torch.backends.cudnn.version()}")
    print(f"✅ GPU Count: {torch.cuda.device_count()}")
    
    for i in range(torch.cuda.device_count()):
        print(f"\n📊 GPU {i}: {torch.cuda.get_device_name(i)}")
        props = torch.cuda.get_device_properties(i)
        print(f"   Total Memory: {props.total_memory / 1e9:.2f} GB")
        print(f"   Compute Capability: {props.major}.{props.minor}")
        
        # Check current memory usage
        print(f"   Allocated: {torch.cuda.memory_allocated(i) / 1e9:.2f} GB")
        print(f"   Cached: {torch.cuda.memory_reserved(i) / 1e9:.2f} GB")
else:
    print("\n⚠️  CUDA is NOT available!")
    print("\nPossible reasons:")
    print("1. PyTorch CPU-only version installed")
    print("2. NVIDIA drivers not installed")
    print("3. CUDA toolkit not installed")
    print("\n💡 Solutions:")
    print("1. Install GPU version of PyTorch:")
    print("   pip uninstall torch")
    print("   pip install torch --index-url https://download.pytorch.org/whl/cu121")
    print("\n2. Check NVIDIA driver:")
    print("   nvidia-smi")
    print("\n3. Check CUDA toolkit:")
    print("   nvcc --version")

# Test basic tensor operations
print("\n" + "=" * 60)
print("🧪 TESTING GPU")
print("=" * 60)

if torch.cuda.is_available():
    try:
        # Create a tensor on GPU
        x = torch.randn(1000, 1000, device='cuda')
        y = torch.randn(1000, 1000, device='cuda')
        
        print("\n⏱️  Testing matrix multiplication on GPU...")
        import time
        start = time.time()
        z = torch.matmul(x, y)
        torch.cuda.synchronize()
        elapsed = time.time() - start
        
        print(f"✅ GPU test passed! ({elapsed*1000:.2f}ms)")
        print(f"✅ Result shape: {z.shape}")
        
        # Show GPU memory after test
        print(f"\n💾 GPU Memory after test:")
        print(f"   Allocated: {torch.cuda.memory_allocated(0) / 1e9:.4f} GB")
        print(f"   Cached: {torch.cuda.memory_reserved(0) / 1e9:.4f} GB")
        
    except Exception as e:
        print(f"\n❌ GPU test failed: {e}")
else:
    print("\n⚠️  Skipping GPU test (CUDA not available)")

# Check transformers library
print("\n" + "=" * 60)
print("🤖 CHECKING TRANSFORMERS")
print("=" * 60)

try:
    import transformers
    print(f"\n✅ Transformers installed: {transformers.__version__}")
    
    # Check if accelerate is installed
    try:
        import accelerate
        print(f"✅ Accelerate installed: {accelerate.__version__}")
    except ImportError:
        print("⚠️  Accelerate not installed (recommended)")
        print("   Install with: pip install accelerate")
    
    # Check if bitsandbytes is installed
    try:
        import bitsandbytes
        print(f"✅ BitsAndBytes installed: {bitsandbytes.__version__}")
    except ImportError:
        print("⚠️  BitsAndBytes not installed (needed for quantization)")
        print("   Install with: pip install bitsandbytes")
        
except ImportError:
    print("\n❌ Transformers not installed!")
    print("Install with: pip install transformers")

print("\n" + "=" * 60)
print("📋 SUMMARY")
print("=" * 60)

if torch.cuda.is_available():
    print("\n✅ GPU is ready to use!")
    print("   Your model will automatically use the GPU.")
else:
    print("\n❌ GPU is NOT available")
    print("   Model will run on CPU (much slower)")
    print("\n   Fix by installing GPU-enabled PyTorch:")
    print("   pip uninstall torch")
    print("   pip install torch --index-url https://download.pytorch.org/whl/cu121")

print("\n")
