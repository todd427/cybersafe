# Red Flag Detection Improvements

## Changes Made

### 1. Fixed Keyword Conflicts
**Problem:** "verify" was in both `questions_sender` and `asks_for_proof`, causing incorrect detection.

**Solution:** Made keywords more specific:
- `questions_sender`: Removed generic "verify", added "is that really you", "is this really"
- `asks_for_proof`: Changed to require explicit proof requests ("show me proof", "need proof")
- `verifies_independently`: Added many variations for independent verification

### 2. Added Call Variations
**Problem:** "I'll call them directly" worked but "I'll call you directly" didn't.

**Solution:** Added both variations:
```python
"verifies_independently": [
    "check myself", "look it up", "verify elsewhere", 
    "call them directly", "call you directly",  # Both variations
    "verify on", "check on instagram", "check on facebook",
    "verify this", "check this myself", "confirm myself"
]
```

### 3. Expanded Verification Keywords
Added phrases that indicate independent verification:
- "verify on [platform]"
- "check on instagram/facebook"
- "verify this"
- "check this myself"
- "confirm myself"

## Test Results

✅ "Is that really you?" → `questions_sender`
✅ "Let me verify this on Instagram" → `verifies_independently`
✅ "I'll call you directly" → `verifies_independently`
✅ "I'll call them directly" → `verifies_independently`

## Current Behavior

When red flags are detected, they display as:
```
🚩 RED FLAG #1 DETECTED: Questions Sender

Sarah:
[AI continues with response...]
```

This is working as designed - the scammer AI responds naturally (trying to deflect, create urgency, etc.) after the red flag is detected.

## Optional Enhancement: Encouraging Feedback

If you want a "Good catch!" message, we could add a system message after each red flag:

```python
flag_msg = f"🚩 RED FLAG #{start_num + i} DETECTED: {flag_name}\n"
yield flag_msg
yield "💡 Good catch! You're staying safe.\n"  # Add this
```

Let me know if you want this added!
