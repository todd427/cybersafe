#!/bin/bash

# Cyber Safer - Professional Upgrade Installation Script
# This script backs up originals and installs all improvements

set -e  # Exit on error

echo "🛡️  Cyber Safer - Professional Upgrade Installer"
echo "=================================================="
echo ""

# Check if we're in the right directory
if [ ! -d "static" ]; then
    echo "❌ Error: static/ directory not found"
    echo "Please run this script from your Cyber Safer root directory"
    exit 1
fi

# Create backups directory
echo "📦 Creating backups..."
mkdir -p backups/$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="backups/$(date +%Y%m%d_%H%M%S)"

# Backup original files
echo "💾 Backing up original files to $BACKUP_DIR..."
[ -f static/categories.html ] && cp static/categories.html "$BACKUP_DIR/"
[ -f static/scenarios.html ] && cp static/scenarios.html "$BACKUP_DIR/"
[ -f static/scenario.html ] && cp static/scenario.html "$BACKUP_DIR/"
[ -f static/chat.html ] && cp static/chat.html "$BACKUP_DIR/"
[ -f static/results.html ] && cp static/results.html "$BACKUP_DIR/"
[ -f cybers.py ] && cp cybers.py "$BACKUP_DIR/"

echo "✅ Backups created"
echo ""

# Check if new files exist
echo "🔍 Checking for upgrade files..."
MISSING=0

if [ ! -f "categories_no_alerts.html" ]; then
    echo "❌ Missing: categories_no_alerts.html"
    MISSING=1
fi

if [ ! -f "scenarios_no_alerts.html" ]; then
    echo "❌ Missing: scenarios_no_alerts.html"
    MISSING=1
fi

if [ ! -f "scenario_no_alerts.html" ]; then
    echo "❌ Missing: scenario_no_alerts.html"
    MISSING=1
fi

if [ ! -f "chat_improved.html" ]; then
    echo "❌ Missing: chat_improved.html"
    MISSING=1
fi

if [ ! -f "results_improved.html" ]; then
    echo "❌ Missing: results_improved.html"
    MISSING=1
fi

if [ ! -f "cybers_fixed.py" ]; then
    echo "❌ Missing: cybers_fixed.py"
    MISSING=1
fi

if [ $MISSING -eq 1 ]; then
    echo ""
    echo "❌ Some upgrade files are missing!"
    echo "Please ensure all upgrade files are in the current directory"
    exit 1
fi

echo "✅ All upgrade files found"
echo ""

# Install new files
echo "🚀 Installing upgraded files..."

cp categories_no_alerts.html static/categories.html
echo "  ✓ Installed categories.html"

cp scenarios_no_alerts.html static/scenarios.html
echo "  ✓ Installed scenarios.html"

cp scenario_no_alerts.html static/scenario.html
echo "  ✓ Installed scenario.html"

cp chat_improved.html static/chat.html
echo "  ✓ Installed chat.html"

cp results_improved.html static/results.html
echo "  ✓ Installed results.html"

cp cybers_fixed.py cybers.py
echo "  ✓ Installed cybers.py (backend)"

echo ""
echo "✅ Installation complete!"
echo ""

# Verify no alerts remain
echo "🔍 Verifying no alert() calls remain..."
ALERT_COUNT=$(grep -r "alert(" static/*.html 2>/dev/null | wc -l)
CONFIRM_COUNT=$(grep -r "confirm(" static/*.html 2>/dev/null | wc -l)

if [ $ALERT_COUNT -eq 0 ] && [ $CONFIRM_COUNT -eq 0 ]; then
    echo "✅ Verification passed - no alerts found!"
else
    echo "⚠️  Warning: Found $ALERT_COUNT alert() and $CONFIRM_COUNT confirm() calls"
    echo "This might be expected in comments or strings"
fi

echo ""
echo "=================================================="
echo "🎉 Professional Upgrade Installed Successfully!"
echo "=================================================="
echo ""
echo "📋 What's new:"
echo "  ✓ No more alert() popups"
echo "  ✓ Professional modal dialogs"
echo "  ✓ Real-time training feedback"
echo "  ✓ Clear success criteria"
echo "  ✓ Progress tracking"
echo "  ✓ Accurate scoring"
echo "  ✓ Loading states everywhere"
echo "  ✓ Better error handling"
echo ""
echo "🚀 Next steps:"
echo "  1. Restart your server:"
echo "     uvicorn cybers:app --reload --port 8021"
echo ""
echo "  2. Open in browser:"
echo "     http://localhost:8021"
echo ""
echo "  3. Test the complete flow:"
echo "     Categories → Online Scams → Dream Job Offer"
echo ""
echo "  4. Verify improvements:"
echo "     - Clear intro with success criteria ✓"
echo "     - Training guide in chat ✓"
echo "     - Real-time feedback messages ✓"
echo "     - Professional modal (not alert) ✓"
echo "     - Accurate score > 0 ✓"
echo ""
echo "📚 Documentation:"
echo "  - NO_ALERTS_GUIDE.md - Complete guide"
echo "  - QUICK_START.md - Quick reference"
echo "  - MASTER_SUMMARY.md - Overview"
echo ""
echo "💾 Your original files are backed up in:"
echo "  $BACKUP_DIR/"
echo ""
echo "Need help? Check the documentation or review the backups."
echo ""
