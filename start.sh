#!/usr/bin/env bash
#
# Cyber Safer - Smart Launcher
# Tests the model first, then starts the server if tests pass
#

set -e  # Exit on error

echo "=================================="
echo "🛡️  Cyber Safer - Smart Launcher"
echo "=================================="
echo ""

# ========== LOAD CONFIG FILE ==========
# Check if config.env exists and load it
if [ -f "config.env" ]; then
    echo "📄 Loading configuration from config.env..."
    source config.env
else
    echo "💡 No config.env found, using defaults"
    echo "   (You can copy config.env.example to config.env to customize)"
fi
echo ""

# ========== CONFIGURATION ==========
# Set default environment variables if not already set

# Model to use (change to smaller model if needed)
export CYBERS_MODEL="${CYBERS_MODEL:-meta-llama/Llama-3.1-8B-Instruct}"

# Quantization bits (4, 8, or empty for none)
export CYBERS_BITS="${CYBERS_BITS:-4}"

# Default player/mentor
export CYBERS_PLAYER="${CYBERS_PLAYER:-players/mentor.json}"

# Server settings
export CYBERS_PORT="${CYBERS_PORT:-8021}"
export CYBERS_HOST="${CYBERS_HOST:-127.0.0.1}"

echo "📋 Active Configuration:"
echo "   Model: $CYBERS_MODEL"
echo "   Quantization: ${CYBERS_BITS}-bit"
echo "   Player: $CYBERS_PLAYER"
echo "   Server: http://${CYBERS_HOST}:${CYBERS_PORT}"
echo ""

# ========== PRE-FLIGHT CHECKS ==========

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi

# Check if uvicorn is available
if ! python3 -c "import uvicorn" 2>/dev/null; then
    echo "❌ uvicorn is not installed"
    echo "💡 Install with: pip install uvicorn"
    exit 1
fi

# Check if required directories exist
if [ ! -d "players" ]; then
    echo "⚠️  Warning: 'players' directory not found"
    echo "   The server may not work correctly"
fi

if [ ! -d "scenarios" ]; then
    echo "⚠️  Warning: 'scenarios' directory not found"
    echo "   The server may not work correctly"
fi

# ========== MODEL TEST ==========

# Step 1: Test model loading
echo "Step 1: Testing model loading..."
echo "--------------------------------"
if python3 test_model.py; then
    echo ""
    echo "✅ Model test passed!"
else
    echo ""
    echo "❌ Model test failed!"
    echo "💡 Fix the issues above before starting the server"
    echo ""
    echo "Common solutions:"
    echo "  - Use smaller model: export CYBERS_MODEL='meta-llama/Llama-3.2-3B-Instruct'"
    echo "  - Use 8-bit quant:   export CYBERS_BITS=8"
    echo "  - Check available RAM/VRAM"
    exit 1
fi

# ========== SERVER START ==========

# Step 2: Start the server
echo ""
echo "Step 2: Starting server..."
echo "--------------------------------"
echo "💡 Press Ctrl+C to stop the server"
echo "💡 Open http://${CYBERS_HOST}:${CYBERS_PORT} in your browser"
echo "💡 In another terminal, run: python test_client.py test"
echo ""

# Give user a moment to read
sleep 2

# Start uvicorn with configured host and port
exec uvicorn cybers:app --reload --host "${CYBERS_HOST}" --port "${CYBERS_PORT}"
