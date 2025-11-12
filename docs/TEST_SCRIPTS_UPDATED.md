# Test Scripts Updated

## Changes Made

Both test scripts have been updated to match the GPU fixes in `cybers.py`.

### test_model.py Changes

**1. Force CUDA Device Mapping**
```python
# OLD:
device_map="auto"

# NEW:
device_map_setting = "cuda" if torch.cuda.is_available() else "auto"
device_map=device_map_setting
```

**2. Verify Model Device**
Added check to ensure model actually loaded to GPU:
```python
if torch.cuda.is_available():
    model_device = next(mdl.parameters()).device
    print(f"   ✅ Model is on: {model_device}")
    if str(model_device) == "cpu":
        print("   ⚠️  WARNING: Model on CPU despite CUDA available!")
```

**3. Explicit Input Device Placement**
```python
# OLD:
inputs = tok([prompt], return_tensors="pt").to(mdl.device)

# NEW:
device = next(mdl.parameters()).device
inputs = tok([prompt], return_tensors="pt")
inputs = {k: v.to(device) for k, v in inputs.items()}
```

**4. Show Device Info During Generation**
```python
print(f"   Model on: {device}")
print(f"   Inputs on: {inputs['input_ids'].device}")
```

### test_client.py

No changes needed - it just makes HTTP requests to the server.

## Why These Changes Matter

Without these fixes, `test_model.py` could show different behavior than the actual server:
- Test might pass on CPU while server fails
- Or test uses GPU while server doesn't
- Inconsistent diagnostics

Now all three files (`cybers.py`, `test_model.py`, and actual server) use the same GPU placement logic.

## Expected Output After Update

When you run `python test_model.py`, you should now see:

```
🛡️  CYBER SAFER - MODEL TEST
📦 Model: meta-llama/Llama-3.1-8B-Instruct
🔧 Quantization: 4-bit
🖥️  Device: CUDA (GPU)
🎮 GPU: NVIDIA GeForce RTX 5060 Ti
💾 GPU Memory: 16.61 GB

⏳ LOADING MODEL (this may take 1-2 minutes)...

1️⃣  Loading tokenizer...
   ✅ Tokenizer loaded

2️⃣  Loading model (largest step, please wait)...
   📍 Device map: cuda
   ✅ Model loaded
   ✅ Model is on: cuda:0  ← CRITICAL CHECK!

📊 Model has 8.03B parameters

3️⃣  TESTING GENERATION

💬 Test prompt: Say 'Hello! The model is working!' and nothing else.
🚀 Generating response...
   Model on: cuda:0
   Inputs on: cuda:0

🤖 Model response: Hello! The model is working!

✅ SUCCESS! Model is working correctly.
```

**Key indicators of success:**
- ✅ `Device map: cuda`
- ✅ `Model is on: cuda:0`
- ✅ `Model on: cuda:0`
- ✅ `Inputs on: cuda:0`

If you see "cpu" anywhere, GPU is NOT being used!

## Verification Checklist

After updating, verify:
- [ ] `test_model.py` shows "Model is on: cuda:0"
- [ ] `test_model.py` shows "Inputs on: cuda:0"
- [ ] No warnings about CPU usage
- [ ] Generation completes in seconds (not minutes)
- [ ] `nvidia-smi` shows GPU usage during test

## Files Updated

✅ `test_model.py` - Updated with GPU fixes
✅ `test_client.py` - No changes needed (already correct)
✅ `cybers.py` - Previously updated with GPU fixes

All three now use consistent GPU placement logic!
