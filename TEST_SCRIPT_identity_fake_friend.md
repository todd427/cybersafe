# Test Script for "identity_fake_friend" Scenario

## Scenario Details

**ID:** identity_fake_friend  
**Title:** Who Are You Really?  
**Category:** Identity Theft  
**Difficulty:** Medium

---

## Success Criteria (Red Flags to Trigger)

You need to demonstrate these 2 behaviors:

1. ✅ **questions_sender** - Question who they really are
2. ✅ **verifies_independently** - Say you'll verify through another way

---

## 📝 Exact Script to Follow

### Initial Message (from "Sarah")
```
Heyyy! It's Sarah from your English class! I got a new phone and lost 
all my contacts 😭 What's your schedule this semester? I think we might 
have lunch at the same time! Also what's your birthday again? We're 
doing a surprise thing for everyone in our friend group lol
```

### Your Response #1 (Trigger "questions_sender")
Say any of these:

**Option A:**
```
Who is this really? I don't think you're Sarah.
```

**Option B:**
```
Are you really from my English class? Can you prove it?
```

**Option C:**
```
This seems suspicious. Who are you?
```

**Keywords that work:**
- "who are you"
- "who is this"
- "verify"
- "prove"
- "real"
- "legitimate"
- "are you really"

✅ **Expected Result:**
- Green message: "✅ Good catch! You demonstrated: Questions Sender"
- Stats update: "Red Flags: 1/2"
- Progress bar: 50%

---

### Your Response #2 (Trigger "verifies_independently")
After the AI responds, say:

**Option A:**
```
I'm going to check with the real Sarah directly
```

**Option B:**
```
Let me verify this with Sarah on another platform
```

**Option C:**
```
I'll look you up on Instagram to confirm
```

**Keywords that work:**
- "check myself"
- "look it up"
- "verify elsewhere"
- "call them directly"
- "check the website"
- "double check"

✅ **Expected Result:**
- Green message: "✅ Good catch! You demonstrated: Verifies Independently"
- Stats update: "Red Flags: 2/2"
- Progress bar: 100%

---

## Complete Interaction Example

```
Sarah (AI):
Heyyy! It's Sarah from your English class! I got a new phone and lost 
all my contacts 😭 What's your schedule this semester?

You:
Who is this really? This seems suspicious.

[✅ Good catch! You demonstrated: Questions Sender]
[Stats: Red Flags: 1/2]

Sarah (AI):
What do you mean? It's me, Sarah! From Mr. Johnson's class...

You:
I'm going to verify this with the real Sarah on Instagram.

[✅ Good catch! You demonstrated: Verifies Independently]
[Stats: Red Flags: 2/2]

Sarah (AI):
[May respond, getting defensive or trying to discourage you]
```

---

## 🎯 What Happens When You Find All Red Flags?

**Short Answer:** No, the scenario does NOT automatically end.

**What Actually Happens:**

1. **Progress Bar:** Fills to 100%
2. **Stats Show:** "Red Flags: 2/2" ✅
3. **Feedback:** Two green success messages
4. **Chat Continues:** You can keep talking
5. **You Decide:** Click "Finish Scenario" when ready

### Why It Doesn't Auto-End

The scenario is designed to let you:
- Practice the conversation more
- See how the scammer reacts when called out
- Learn by continuing the interaction
- Finish when YOU feel ready

### Scoring Impact

When you click "Finish Scenario":
- You get 30 points per required flag (60 total)
- Plus engagement bonus (up to 20 points)
- Plus extra flags bonus (if you detected more)
- **Maximum Score:** 100 points

Finding 2/2 flags typically gives you: **70-80 points** (passing is 60+)

---

## 💡 Tips for Testing

### Additional Red Flags (Bonus Points)

While not required, you can also trigger:

**"questions_personal_info"** (10 bonus points)
- "Why do you need my birthday?"
- "That's too personal"
- "I don't give out that info"

**"asks_for_proof"** (10 bonus points)
- "Can you prove you know me?"
- "Tell me something only Sarah would know"
- "Show me evidence"

### Realistic Practice

Try different approaches:
1. **Direct:** "I don't believe you're Sarah"
2. **Polite:** "Can you tell me something we talked about?"
3. **Cautious:** "I'm going to verify this first"

All teach the same skills but practice different response styles.

---

## 🧪 Complete Test Flow

```
1. Go to: Identity Theft → "Who Are You Really?"
2. Read the intro (sets expectations)
3. Click "Begin Scenario"
4. See training guide showing 2 required flags
5. AI sends first message as "Sarah"
6. Type: "Who is this really?"
7. Watch for green success message ✅
8. Check stats: "1/2" red flags
9. AI responds (may get defensive)
10. Type: "I'll verify with the real Sarah"
11. Watch for second green message ✅
12. Check stats: "2/2" red flags (100% complete)
13. Chat continues - you can keep going
14. Click "Finish Scenario" when ready
15. See results: Score 70-80, "✅ Passed!"
```

---

## 📊 Expected Results

### If You Get Both Flags

**Results Screen Shows:**
```
Score: 75
✅ Passed!

Your Performance:
- 2 Red Flags Detected
- 2 Critical Flags Found
- 2 Total Red Flags

Good effort! You caught 2 out of 2 critical red flags.

Critical Red Flags (Required):
✅ Questions Sender - You spotted this!
✅ Verifies Independently - You spotted this!
```

### If You Miss One

**Results Screen Shows:**
```
Score: 50
📚 Keep Practicing

Your Performance:
- 1 Red Flags Detected
- 1 Critical Flags Found
- 2 Total Red Flags

Making progress! You found 1 out of 2 critical red flags.
Review the one you missed to improve.

Critical Red Flags (Required):
✅ Questions Sender - You spotted this!
❌ Verifies Independently - Missed - watch for this
```

---

## 🎓 Learning Outcomes

After this scenario, students should understand:

✅ **Don't assume identity** - Just because someone uses a name doesn't mean they're real  
✅ **Verify through alternate channels** - Call, message on known account, ask in person  
✅ **Be suspicious of vague details** - Real friends mention specific shared experiences  
✅ **Don't share personal info** - Birthday, schedule, address are security question answers  
✅ **Trust your instincts** - If it feels off, it probably is

---

## 🚨 Common Issues

### "Stats not updating"
- Check browser console for errors
- Make sure keywords match (see lists above)
- Try more explicit phrases: "I don't believe you're really Sarah"

### "No green messages appearing"
- Verify chat_improved.html is installed
- Check that scenario has success_criteria defined
- Clear browser cache and reload

### "Score still 0 at end"
- Check server logs for detection messages
- Verify cybers_fixed.py is installed
- Make sure scenario file has proper success_criteria

---

**Ready to test!** Follow the script above and watch the red flags increment. 🎯
