#!/bin/bash
# Clear GPU memory script

echo "🔍 Checking what's using GPU memory..."
nvidia-smi

echo ""
echo "🔍 Finding Python processes using GPU..."
ps aux | grep python | grep -v grep

echo ""
echo "💡 To kill the process using GPU:"
echo "   kill -9 552474"
echo ""
echo "Or kill ALL Python processes:"
echo "   pkill -9 python"
echo ""
echo "Then try test_model.py again"
