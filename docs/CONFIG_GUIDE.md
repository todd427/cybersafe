# Configuration Guide

## Quick Setup

1. **Copy the example config:**
   ```bash
   cp config.env.example config.env
   ```

2. **Edit settings in `config.env`:**
   ```bash
   nano config.env    # or use any text editor
   ```

3. **Start the server:**
   ```bash
   ./start.sh
   ```

The script will automatically load your `config.env` file!

## Configuration Options

### Model Selection

**`CYBERS_MODEL`** - Which AI model to use

| Model | RAM Needed | Quality | Use Case |
|-------|------------|---------|----------|
| `meta-llama/Llama-3.2-1B-Instruct` | ~2GB | Basic | Testing, low-end systems |
| `meta-llama/Llama-3.2-3B-Instruct` | ~4GB | Good | Balanced, most systems |
| `meta-llama/Llama-3.1-8B-Instruct` | ~8GB | Best | Default, recommended |
| `Qwen/Qwen2.5-7B-Instruct` | ~7GB | Excellent | Alternative option |

### Quantization

**`CYBERS_BITS`** - Memory compression level

| Value | VRAM Usage | Quality | Notes |
|-------|------------|---------|-------|
| `4` | ~4GB | Good | Default, best for most |
| `8` | ~8GB | Better | If you have enough RAM |
| `""` | ~16GB | Best | Full precision, no compression |

### Server Settings

**`CYBERS_PORT`** - Port number (default: 8021)
**`CYBERS_HOST`** - Bind address:
- `127.0.0.1` - Local only (default, secure)
- `0.0.0.0` - Allow external access (use with caution)

## Presets

The `config.env.example` file includes presets you can uncomment:

### Low Memory Preset
For systems with <8GB RAM:
```bash
export CYBERS_MODEL="meta-llama/Llama-3.2-1B-Instruct"
export CYBERS_BITS="4"
```

### Balanced Preset (Default)
For systems with 8-16GB RAM:
```bash
export CYBERS_MODEL="meta-llama/Llama-3.1-8B-Instruct"
export CYBERS_BITS="4"
```

### High Quality Preset
For systems with 16GB+ RAM:
```bash
export CYBERS_MODEL="meta-llama/Llama-3.1-8B-Instruct"
export CYBERS_BITS="8"
```

### CPU Only Preset
No GPU available:
```bash
export CYBERS_MODEL="meta-llama/Llama-3.2-3B-Instruct"
export CYBERS_BITS="8"
```

## Advanced Settings

### HuggingFace Cache
Models are cached to avoid re-downloading:
```bash
export HF_HOME="$HOME/.cache/huggingface"
```

### PyTorch CUDA Memory
For better GPU memory management:
```bash
export PYTORCH_CUDA_ALLOC_CONF="max_split_size_mb:512"
```

### CPU Threads
For CPU inference:
```bash
export OMP_NUM_THREADS="8"
```

## Testing Your Configuration

After changing settings:

1. **Test the model:**
   ```bash
   python test_model.py
   ```

2. **If it works, start the server:**
   ```bash
   ./start.sh
   ```

3. **Test the server:**
   ```bash
   python test_client.py test
   ```

## Troubleshooting

### Out of Memory
- Use a smaller model
- Increase quantization (4-bit)
- Close other applications

### Slow Generation
- Use a smaller model
- Check if using GPU (should say "Device: CUDA")
- Verify system isn't swapping

### Model Not Found
- Check model name spelling
- Ensure internet connection (first download)
- Check HuggingFace is accessible

### Can't Connect to Server
- Check firewall settings
- Verify port isn't in use: `lsof -i :8021`
- Try a different port

## Example Configurations

### Home Server (accessible from network)
```bash
export CYBERS_MODEL="meta-llama/Llama-3.1-8B-Instruct"
export CYBERS_BITS="4"
export CYBERS_HOST="0.0.0.0"
export CYBERS_PORT="8021"
```

### Development (local only, small model)
```bash
export CYBERS_MODEL="meta-llama/Llama-3.2-3B-Instruct"
export CYBERS_BITS="4"
export CYBERS_HOST="127.0.0.1"
export CYBERS_PORT="8021"
```

### Production (best quality)
```bash
export CYBERS_MODEL="meta-llama/Llama-3.1-8B-Instruct"
export CYBERS_BITS="8"
export CYBERS_HOST="127.0.0.1"
export CYBERS_PORT="8021"
```

## Tips

1. **Start with defaults** - They work for most systems
2. **Test before committing** - Use `test_model.py` first
3. **Monitor resources** - Watch RAM/VRAM usage
4. **Keep config.env private** - Don't commit to git
5. **Document your changes** - Comment your custom settings

Need help? See `TESTING_GUIDE.md` for detailed troubleshooting!
