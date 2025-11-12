# Complete Fix for Red Flag Detection Issues

## Problems Fixed

### 1. "Is that you, really?" Not Detected ✅
**Problem:** Word order and punctuation variations weren't recognized.

**Solution:** Added variations including:
- "is that you," (with comma)
- "is that you really" 
- "who is that"
- "are you actually"
- "is this actually"

### 2. "check you on Instagram" Variations ✅
**Problem:** Only "check on Instagram" worked, not "check you on"

**Solution:** Added:
- "check you on"
- "verify you on"
- These catch "check you on Instagram" and similar phrases

### 3. Counter Not Updating ❌ (Needs Frontend Changes)
**Problem:** Red flags are detected but the "Red Flags Found: 1/2" counter doesn't update.

**Root Cause:** 
- Backend correctly detects flags and stores them
- Frontend displays the initial counter but doesn't update it
- No communication channel for real-time counter updates

**Backend Solution (Implemented):**
1. Added `[COUNTER:X/Y]` marker in stream response
2. Added `/api/scenario/status` endpoint for polling

**Frontend Solution (Needs Implementation):**
Choose one of two approaches:

#### Approach A: Parse Stream Markers (Recommended)
The backend now sends `[COUNTER:1/2]` before each red flag alert.
Frontend needs to:
1. Detect this marker in the stream
2. Extract the numbers
3. Update the counter display
4. Remove the marker before showing the message

See `frontend_counter_patch.js` for implementation.

#### Approach B: Poll Status Endpoint
Frontend can poll `/api/scenario/status` every 2 seconds:
```javascript
GET /api/scenario/status
Response: {
  "active": true,
  "red_flags_found": 2,
  "red_flags_required": 2,
  "all_detected_flags": ["questions_sender", "verifies_independently"]
}
```

## Testing

After applying all fixes:

### Test Case 1: Question Variations
```
User: "Is that you, really?"
Expected: ✅ Questions Sender detected
Counter: 1/2
```

```
User: "Who is that?"
Expected: ✅ Questions Sender detected  
Counter: 1/2
```

### Test Case 2: Verification Variations
```
User: "I'm going to check you on Instagram"
Expected: ✅ Verifies Independently detected
Counter: 2/2
```

```
User: "Let me verify you on Facebook"
Expected: ✅ Verifies Independently detected
Counter: 2/2 (if both required flags met)
```

## Current Status

✅ Backend keyword detection - FIXED
✅ API endpoints - FIXED
✅ Stream markers - IMPLEMENTED
❌ Frontend counter update - NEEDS IMPLEMENTATION

## Next Steps

1. Update `static/chat.html` or wherever the message streaming happens
2. Add the counter update logic from `frontend_counter_patch.js`
3. Ensure the counter element has an ID: `<span id="redFlagCounter">1/2</span>`
4. Test with various phrasings

## Keywords Reference

Current detection keywords:

**questions_sender:**
- "who are you", "who is this", "who is that"
- "are you really", "is that really you", "is that you really", "is that you,"
- "is this really", "are you actually", "is this actually"
- "prove who you", "prove you're", "prove this is"

**verifies_independently:**
- "check myself", "look it up", "verify elsewhere"
- "call them directly", "call you directly"
- "verify on", "verify you on", "check on instagram", "check you on"
- "verify this", "check this myself", "confirm myself"

**asks_for_proof:**
- "show me proof", "need proof", "provide evidence", "show evidence"
