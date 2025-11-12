# Missing Player Files - Quick Fix

## Problem
Your scenario `identity_fake_friend` is looking for `players/fake_friend.json` but it doesn't exist.

## Solution

Copy this file to your `players/` directory:

**File:** `fake_friend.json`

This player file is already created and ready to use.

## Installation

```bash
# Copy the missing player file
cp fake_friend.json players/

# Restart your server
uvicorn cybers:app --reload --port 8021
```

## Verification

After copying, you should see:
```
📚 Loaded scenario: Who Are You Really?
✅ Scenario starts without "Could not load player" error
```

## All Player Files Needed

Based on your scenarios, you should have these player files:

✅ **Already Have (from context):**
- `mentor.json` - Friendly guide
- `phishing_emailer.json` - Fake security/bank rep
- `romance_scammer.json` - Online romance scammer
- `tech_support_scammer.json` - Fake tech support
- `cyberbully.json` - Cyberbully antagonist

❌ **Missing (now provided):**
- `fake_friend.json` - Identity thief posing as classmate

## Player File Format

All player files follow this structure:
```json
{
  "name": "Character Name",
  "profession": "Role description",
  "personality": "Personality traits",
  "style": "Communication style",
  "facts_guard": false,
  "instructions": "Detailed instructions for AI",
  "max_tokens": 180,
  "temperature": 0.77,
  "top_p": 0.9
}
```

## Testing

After installation:
1. Go to Identity Theft category
2. Click "Who Are You Really?"
3. Should start without errors
4. AI should act as "Sarah" pretending to be a classmate

---

**The fake_friend.json file is ready in your outputs folder!**
