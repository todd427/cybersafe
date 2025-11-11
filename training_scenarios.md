# Complete Scenario Collection for Cyber Safer

Save each JSON block as a separate file in `scenarios/` directory.

---

## PHISHING (3 scenarios)

### phishing_urgent_email.json (already have)
```json
{
  "id": "phishing_urgent_email",
  "category": "phishing",
  "difficulty": "beginner",
  "title": "The Urgent Account Security Email",
  "introduction": "You've just received an email claiming to be from your bank. It says your account has been compromised and you need to act immediately. The email looks official with the bank's logo and professional language. What do you do?",
  "player": "phishing_emailer",
  "initial_message": "URGENT: Your account has been compromised!\n\nDear Valued Customer,\n\nWe've detected suspicious activity on your account. For your security, you must verify your identity within 24 hours or your account will be permanently locked.\n\nClick here to verify now: http://totally-real-bank-security.com/verify\n\nThank you,\nCustomer Security Team",
  "red_flags": [
    "questions_sender",
    "refuses_to_click",
    "checks_url",
    "reports_phishing",
    "questions_urgency"
  ],
  "success_criteria": [
    "questions_sender",
    "refuses_to_click"
  ],
  "learning_objectives": [
    "Recognize urgency tactics used in phishing",
    "Question sender authenticity",
    "Avoid clicking suspicious links",
    "Know how to report phishing attempts"
  ],
  "debrief": "Great job! This was a classic phishing attempt. The red flags were: 1) Creating urgency with threats, 2) Suspicious URL that doesn't match the real bank's website, 3) Generic greeting instead of your name. Real banks never ask you to verify via email links. Always go directly to the official website or call the number on your card."
}
```

### phishing_prize_winner.json
```json
{
  "id": "phishing_prize_winner",
  "category": "phishing",
  "difficulty": "beginner",
  "title": "Congratulations, You've Won!",
  "introduction": "You receive a text message saying you've won a $500 gift card from a popular store. All you need to do is click a link and enter some information to claim your prize. Sounds great, right?",
  "player": "phishing_emailer",
  "initial_message": "🎉 CONGRATULATIONS! You've been selected as a WINNER in our monthly drawing! You've won a $500 Amazon gift card!\n\nClaim your prize now: http://amaz0n-prizes.com/claim?id=847392\n\nHurry! This link expires in 3 hours!\n\n-Amazon Prize Center",
  "red_flags": [
    "questions_sender",
    "refuses_to_click",
    "checks_url",
    "questions_urgency",
    "verifies_independently"
  ],
  "success_criteria": [
    "questions_sender",
    "refuses_to_click"
  ],
  "learning_objectives": [
    "Recognize too-good-to-be-true offers",
    "Check URLs carefully for slight misspellings",
    "Understand that legitimate companies don't notify winners via random texts",
    "Verify contests independently"
  ],
  "debrief": "Well done! This was a phishing scam using fake prizes. Red flags: 1) You didn't enter any contest, 2) URL uses '0' instead of 'o' in Amazon, 3) Creating false urgency with expiration, 4) Real companies notify winners differently. If it seems too good to be true, it usually is. Always verify contest wins through official channels."
}
```

### phishing_friend_help.json
```json
{
  "id": "phishing_friend_help",
  "category": "phishing",
  "difficulty": "medium",
  "title": "Friend in Trouble",
  "introduction": "You get a message from someone claiming to be your friend. They say they're stranded and desperately need money. The message seems urgent and emotional. But something feels off...",
  "player": "phishing_emailer",
  "initial_message": "hey its me!!! my phone died and im using a friends phone. im stranded at the mall and my parents arent answering. can you PLEASE send me $50 through cashapp?? ill pay you back tomorrow i promise. my cashapp is $QuickCash847. im freaking out please help!!",
  "red_flags": [
    "questions_sender",
    "refuses_money",
    "verifies_independently",
    "questions_urgency",
    "asks_for_proof"
  ],
  "success_criteria": [
    "questions_sender",
    "verifies_independently"
  ],
  "learning_objectives": [
    "Verify identity before helping with money",
    "Recognize emotional manipulation",
    "Know how to verify identity through alternate channels",
    "Understand that real friends won't pressure you this way"
  ],
  "debrief": "Good thinking! This was a phishing attempt impersonating a friend. Red flags: 1) Using a 'friend's phone' makes verification harder, 2) Urgency and emotional pressure, 3) Generic CashApp tag not linked to friend, 4) Real friend would call parents or use other options first. Always verify through a different method - call them, message on another platform, or check with mutual friends before sending money."
}
```

---

## ONLINE SCAMS (3 scenarios)

### scam_romance_lonely.json
```json
{
  "id": "scam_romance_lonely",
  "category": "online_scams",
  "difficulty": "medium",
  "title": "Too Good to Be True",
  "introduction": "You've been chatting with someone online who seems really interested in you. They're attractive, charming, and say all the right things. After a week, they start talking about their problems...",
  "player": "romance_scammer",
  "initial_message": "Hey! I've been thinking about you all day 😊 You're honestly so different from everyone else I've talked to. You really get me, you know? I feel like we have such a special connection already. Can I tell you something personal?",
  "red_flags": [
    "questions_personal_info",
    "refuses_money",
    "recognizes_manipulation",
    "verifies_independently",
    "tells_adult"
  ],
  "success_criteria": [
    "recognizes_manipulation",
    "refuses_money"
  ],
  "learning_objectives": [
    "Recognize love bombing and fast emotional connection",
    "Identify when requests for money appear",
    "Understand romance scam patterns",
    "Know it's okay to slow down online relationships"
  ],
  "debrief": "Smart! This was a romance scam. Red flags: 1) Moving too fast emotionally, 2) Excessive flattery and claims of special connection, 3) Will soon ask for money or gift cards, 4) Creates dependency quickly. Real relationships develop slowly. Be suspicious of anyone online who professes strong feelings quickly or asks for money. Talk to a trusted adult if someone pressures you this way."
}
```

### scam_investment_quick.json
```json
{
  "id": "scam_investment_quick",
  "category": "online_scams",
  "difficulty": "medium",
  "title": "Get Rich Quick",
  "introduction": "You see an ad on social media about making easy money. A teen just like you claims they made $2000 in a week just by investing $100. They're messaging people offering to help them do the same...",
  "player": "romance_scammer",
  "initial_message": "Yo! Saw your profile and thought you might be interested in making some real money. I'm 17 and I made $2000 last week through crypto investing. It's super easy, I can teach you. You just need to start with $100 and I'll show you exactly what to do. My mentor has a special system. Want in?",
  "red_flags": [
    "questions_urgency",
    "refuses_money",
    "verifies_independently",
    "asks_for_proof",
    "tells_adult"
  ],
  "success_criteria": [
    "refuses_money",
    "asks_for_proof"
  ],
  "learning_objectives": [
    "Recognize 'get rich quick' schemes",
    "Understand that real investments require knowledge and risk",
    "Identify pyramid scheme patterns",
    "Know to be suspicious of unsolicited money offers"
  ],
  "debrief": "Excellent! This was an investment scam. Red flags: 1) Promises of easy/quick money, 2) Pressure to invest now, 3) Unsolicited approach with 'special system', 4) Asking for money upfront. Real investing requires research, has risks, and no one offers strangers guaranteed money. These scams either take your money directly or get you to recruit others. Always talk to parents before any money decisions."
}
```

### scam_job_offer.json
```json
{
  "id": "scam_job_offer",
  "category": "online_scams",
  "difficulty": "beginner",
  "title": "Dream Job Offer",
  "introduction": "You get an email about a part-time job that seems perfect - work from home, flexible hours, great pay. They want to hire you immediately. You just need to provide some information and pay for training materials first...",
  "player": "phishing_emailer",
  "initial_message": "Dear Applicant,\n\nCongratulations! We reviewed your profile and you're a perfect fit for our Remote Social Media Manager position. $25/hour, work from home, only 10 hours/week!\n\nTo get started, we need:\n- Full name and address\n- Social Security Number (for payroll)\n- $49 for training materials (refundable after first paycheck)\n\nStart earning TODAY! Reply with your information to begin.\n\n-HR Department, Digital Success Inc.",
  "red_flags": [
    "questions_sender",
    "refuses_money",
    "questions_personal_info",
    "verifies_independently",
    "tells_adult"
  ],
  "success_criteria": [
    "refuses_money",
    "questions_personal_info"
  ],
  "learning_objectives": [
    "Recognize job scams",
    "Know that real employers don't ask for money",
    "Understand SSN should never be given before proper hiring",
    "Learn to research companies before applying"
  ],
  "debrief": "Great job! This was a job scam. Red flags: 1) Hired without application or interview, 2) Asking for Social Security Number too early, 3) Requiring payment for 'training materials', 4) Too good to be true pay for simple work. Real employers never ask for money. They pay you for training. Always research companies and discuss job opportunities with parents first."
}
```

---

## IDENTITY THEFT (3 scenarios)

### identity_fake_friend.json
```json
{
  "id": "identity_fake_friend",
  "category": "identity_theft",
  "difficulty": "medium",
  "title": "Who Are You Really?",
  "introduction": "Someone claiming to be a classmate messages you on social media. They seem to know things about your school and mutual friends. They're asking questions about your personal life and want to connect...",
  "player": "fake_friend",
  "initial_message": "Heyyy! It's Sarah from your English class! I got a new phone and lost all my contacts 😭 What's your schedule this semester? I think we might have lunch at the same time! Also what's your birthday again? We're doing a surprise thing for everyone in our friend group lol",
  "red_flags": [
    "questions_sender",
    "questions_personal_info",
    "verifies_independently",
    "asks_for_proof"
  ],
  "success_criteria": [
    "questions_sender",
    "verifies_independently"
  ],
  "learning_objectives": [
    "Verify identity of online contacts",
    "Recognize fishing for personal information",
    "Know what information is risky to share",
    "Use alternate channels to verify identity"
  ],
  "debrief": "Smart thinking! This was an identity thief posing as a classmate. Red flags: 1) Vague about specific shared experiences, 2) Asking for birthday and schedule (security question answers and patterns), 3) 'New phone' excuse to explain not having your number, 4) Using common names and scenarios. Always verify through another channel - ask them something only the real person would know, or contact them through a known account. Never give personal info to unverified contacts."
}
```

### identity_social_quiz.json
```json
{
  "id": "identity_social_quiz",
  "category": "identity_theft",
  "difficulty": "beginner",
  "title": "Fun Quiz or Data Mining?",
  "introduction": "A fun-looking quiz is going viral on social media: 'Your Superhero Name Generator!' It asks for your mother's maiden name, the street you grew up on, and your first pet's name. Sounds harmless, right?",
  "player": "fake_friend",
  "initial_message": "OMG you HAVE to try this quiz!! It's so fun! 🦸\n\nFind Your SUPERHERO NAME:\n1. Mother's maiden name = First name\n2. Street you grew up on = Last name  \n3. First pet's name = Power name\n4. Birth month = Your origin story\n\nPost yours in the comments! Mine is 'Jennifer Oakwood with Fire Powers, origin: December' 😂 What's yours??",
  "red_flags": [
    "questions_personal_info",
    "recognizes_manipulation",
    "refuses_to_click"
  ],
  "success_criteria": [
    "questions_personal_info",
    "recognizes_manipulation"
  ],
  "learning_objectives": [
    "Recognize that common security questions are being asked",
    "Understand how 'fun' quizzes can steal identity",
    "Know what information is used for password recovery",
    "Think before sharing personal data"
  ],
  "debrief": "Excellent! You spotted the trap! This 'fun quiz' is actually collecting common security question answers. Red flags: 1) Mother's maiden name - classic security question, 2) Street you grew up on - another common security question, 3) First pet - also used for password recovery, 4) Birth month adds to profile. Scammers use this info to break into accounts or steal identity. These quizzes seem fun but are data mining. Don't share answers to security questions publicly."
}
```

### identity_account_takeover.json
```json
{
  "id": "identity_account_takeover",
  "category": "identity_theft",
  "difficulty": "hard",
  "title": "Help Me Recover My Account",
  "introduction": "A message pops up claiming to be from Instagram support. They say your account is being reported and might be deleted unless you verify ownership. They need you to prove you're the real owner...",
  "player": "fake_friend",
  "initial_message": "⚠️ INSTAGRAM SECURITY ALERT ⚠️\n\nYour account has been reported for suspicious activity and may be permanently deleted within 24 hours.\n\nTo verify you are the legitimate owner, please provide:\n- Current password\n- Email associated with account\n- Phone number\n- Date of birth\n\nReply quickly to prevent account deletion.\n\nInstagram Security Team\nCase #IG-77382",
  "red_flags": [
    "questions_sender",
    "questions_personal_info",
    "questions_urgency",
    "verifies_independently",
    "reports_phishing"
  ],
  "success_criteria": [
    "questions_sender",
    "verifies_independently"
  ],
  "learning_objectives": [
    "Know that real platforms never ask for passwords",
    "Recognize account takeover attempts",
    "Understand how to verify official communications",
    "Learn where to check for real security alerts"
  ],
  "debrief": "Perfect! This was an account takeover scam. Red flags: 1) Instagram never asks for your password, 2) Creating panic with deletion threat, 3) Random message instead of in-app notification, 4) Asking for all account security info. Real security alerts appear inside the app, not via random messages. Social media companies never ask for passwords. Always check inside the actual app for security notifications. If concerned, go directly to the app or website - never through links in messages."
}
```

---

## CYBERBULLYING (3 scenarios)

### bully_threat_share.json
```json
{
  "id": "bully_threat_share",
  "category": "cyberbullying",
  "difficulty": "medium",
  "title": "I Have Screenshots",
  "introduction": "Someone messages you saying they have embarrassing screenshots of your old social media posts and will share them with everyone at school unless you do what they want. You feel panicked and afraid...",
  "player": "cyberbully",
  "initial_message": "Hey loser. I have screenshots of your old cringey posts from like 2 years ago. You know the ones 😏 They're SO embarrassing. I'm gonna send them to EVERYONE unless you do exactly what I say. Better start being nicer to me at school. And I want your lunch money this week. Or everyone sees the screenshots. Your choice.",
  "red_flags": [
    "blocks_contact",
    "tells_adult",
    "recognizes_manipulation",
    "reports_phishing"
  ],
  "success_criteria": [
    "tells_adult",
    "blocks_contact"
  ],
  "learning_objectives": [
    "Recognize extortion and threats",
    "Know that giving in makes it worse",
    "Understand importance of telling trusted adults",
    "Learn to document and report bullying"
  ],
  "debrief": "You handled that well! This was cyberbullying and extortion. Red flags: 1) Threatening to embarrass you, 2) Demanding things (money, changed behavior), 3) Using fear to control you. Important: Giving bullies what they want never stops them - it makes it worse. The right steps: 1) Don't engage or give in, 2) Screenshot the threats as evidence, 3) Block them, 4) Tell a trusted adult immediately (parent, counselor, principal). This is serious and adults can help. Most importantly - everyone has embarrassing old posts. Real friends won't care."
}
```

### bully_group_exclusion.json
```json
{
  "id": "bully_group_exclusion",
  "category": "cyberbullying",
  "difficulty": "beginner",
  "title": "Left Out of the Group",
  "introduction": "You notice you've been removed from the group chat. Then someone sends you mean messages saying no one likes you and everyone has been talking about you behind your back. They want you to know everyone thinks you're annoying...",
  "player": "cyberbully",
  "initial_message": "Just thought you should know everyone was talking about you in the group chat after we removed you. They all think you're super annoying and fake. Like literally NO ONE wants you around. Maya said you try too hard and Jake was laughing about your outfit yesterday. Just giving you a heads up so you stop embarrassing yourself. 🙄",
  "red_flags": [
    "blocks_contact",
    "tells_adult",
    "recognizes_manipulation"
  ],
  "success_criteria": [
    "recognizes_manipulation",
    "tells_adult"
  ],
  "learning_objectives": [
    "Recognize social manipulation and rumors",
    "Understand that bullies lie to hurt feelings",
    "Know the difference between friends and bullies",
    "Learn that real friends communicate directly"
  ],
  "debrief": "Good job staying strong! This was social cyberbullying through exclusion and rumors. Red flags: 1) Claiming to speak for others, 2) Using specific names to make it seem real, 3) Trying to hurt your self-esteem, 4) 'Just giving you a heads up' - fake kindness that's actually mean. Reality check: Bullies often lie about what others said. Real friends don't remove you and mock you - they talk to you directly about issues. This behavior says more about the bully than you. Talk to a trusted adult about social bullying. Consider whether this group is worth your energy."
}
```

### bully_photo_threat.json
```json
{
  "id": "bully_photo_threat",
  "category": "cyberbullying",
  "difficulty": "hard",
  "title": "I'll Share Your Photo",
  "introduction": "Someone has an embarrassing photo of you from a party. They're threatening to post it publicly and tag you so everyone sees it unless you give them what they want. You're scared about your reputation...",
  "player": "cyberbully",
  "initial_message": "Remember that photo from the party last week? The really embarrassing one? 📸 I'm about to post it on Instagram and tag you and everyone we know. Unless... you make it worth my while not to. I'm thinking you could do my homework for the next month? OR I could just post it right now. What's it gonna be? Clock's ticking.",
  "red_flags": [
    "blocks_contact",
    "tells_adult",
    "recognizes_manipulation",
    "reports_phishing"
  ],
  "success_criteria": [
    "tells_adult",
    "blocks_contact"
  ],
  "learning_objectives": [
    "Recognize serious cyberbullying and extortion",
    "Know this may be illegal (depending on photo)",
    "Understand importance of immediate adult help",
    "Learn about consequences for the bully"
  ],
  "debrief": "You did the right thing by getting help! This is serious cyberbullying and potentially illegal. Red flags: 1) Extortion (demanding something under threat), 2) Using embarrassment as weapon, 3) Time pressure to force bad decisions. Critical points: 1) NEVER give in to threats - it won't stop, 2) Tell parent/school counselor/principal IMMEDIATELY, 3) This is potentially criminal depending on the photo, 4) The bully can face serious consequences. Document everything. Schools and sometimes police take this seriously. You're not alone - adults can and will help stop this."
}
```

---

## MALWARE & RANSOMWARE (3 scenarios)

### malware_free_game.json
```json
{
  "id": "malware_free_game",
  "category": "malware",
  "difficulty": "beginner",
  "title": "Free Game Download",
  "introduction": "You really want to play a popular game that costs $60. You find a website offering it for free download. The site looks a bit sketchy but the download button is right there...",
  "player": "tech_support_scammer",
  "initial_message": "🎮 GET ANY GAME FREE! 🎮\n\nDownload [Popular Game] for FREE! No payment required!\n\nClick the big green DOWNLOAD button below. File size: 15MB\n\nNote: Your antivirus might say it's unsafe but that's normal for cracked games. Just click 'Allow' or disable your antivirus temporarily.\n\n[DOWNLOAD FREE GAME NOW]",
  "red_flags": [
    "refuses_to_click",
    "questions_sender",
    "verifies_independently",
    "tells_adult"
  ],
  "success_criteria": [
    "refuses_to_click",
    "verifies_independently"
  ],
  "learning_objectives": [
    "Understand piracy risks beyond legal issues",
    "Recognize malware distribution methods",
    "Know that legitimate software doesn't ask you to disable antivirus",
    "Learn about safe software sources"
  ],
  "debrief": "Smart choice! This was malware disguised as a free game. Red flags: 1) 'Free' version of paid software is piracy and illegal, 2) Telling you to ignore antivirus warnings is a HUGE red flag, 3) File size too small for a real game, 4) Sketchy website instead of official store. Malware can steal passwords, install ransomware, or use your computer for illegal activity. The 'free' game could cost you way more in damages. Only download from official sources: Steam, App Store, official websites. If you can't afford something, ask parents or wait for sales."
}
```

### malware_system_warning.json
```json
{
  "id": "malware_system_warning",
  "category": "malware",
  "difficulty": "medium",
  "title": "Your Computer Is Infected",
  "introduction": "A pop-up suddenly appears on your screen claiming your computer is infected with viruses. It's showing scary warnings and says you need to call a number immediately or download a security program to fix it...",
  "player": "tech_support_scammer",
  "initial_message": "⚠️ CRITICAL SECURITY ALERT ⚠️\n\nYour computer is infected with (4) viruses!\n\nThreats detected:\n- Trojan.Win32.Danger\n- Malware.Generic.PWS\n- System corruption detected\n\nYour personal data, passwords, and files are at risk!\n\nCALL NOW: 1-800-FIX-COMPUTER\nOr DOWNLOAD FIX TOOL immediately!\n\nDO NOT SHUT DOWN YOUR COMPUTER\n\n[Download CleanPro Security] [Call Support]",
  "red_flags": [
    "refuses_to_click",
    "questions_sender",
    "verifies_independently",
    "tells_adult"
  ],
  "success_criteria": [
    "refuses_to_click",
    "tells_adult"
  ],
  "learning_objectives": [
    "Recognize fake security warnings",
    "Understand that real antivirus doesn't work through pop-ups",
    "Know how to close fake warnings safely",
    "Learn the difference between real and fake alerts"
  ],
  "debrief": "Excellent! This was a fake security warning (scareware). Red flags: 1) Real antivirus doesn't use pop-ups with phone numbers, 2) Creating panic with capitals and urgent warnings, 3) Asking you to download unknown software or call random number, 4) Real security software is already on your computer - it doesn't advertise through web pop-ups. Right action: Close the browser (don't click anything in the pop-up), run your ACTUAL antivirus if worried, tell a parent. These fake warnings either install malware or lead to phone scams. Real security is quiet and professional, not scary and loud."
}
```

### malware_email_attachment.json
```json
{
  "id": "malware_email_attachment",
  "category": "malware",
  "difficulty": "medium",
  "title": "Suspicious Email Attachment",
  "introduction": "You get an email that looks like it's from your school. The subject says 'Important: Updated Class Schedule' and includes an attachment named 'Schedule_2024.exe'. Should you open it to check your new schedule?",
  "player": "tech_support_scammer",
  "initial_message": "From: admin@schooldistrict-portal.com\nSubject: IMPORTANT: Updated Class Schedule\n\nDear Student,\n\nYour class schedule has been updated for the new semester. Please open the attached file to view your new schedule immediately.\n\nAttachment: Schedule_2024.exe (2.1 MB)\n\nIf you have trouble opening the file, right-click and select 'Run as Administrator'.\n\nThank you,\nSchool Administration",
  "red_flags": [
    "refuses_to_click",
    "checks_url",
    "questions_sender",
    "verifies_independently",
    "tells_adult"
  ],
  "success_criteria": [
    "refuses_to_click",
    "checks_url"
  ],
  "learning_objectives": [
    "Recognize dangerous file extensions",
    "Understand .exe files can be malware",
    "Know how schools actually send schedules",
    "Learn to verify sender email addresses"
  ],
  "debrief": "Great catch! This email contained malware. Red flags: 1) .exe file extension - this is an executable program, NOT a document, 2) Schools send schedules as PDF or in student portals, never as .exe files, 3) Email domain looks similar but isn't the real school domain, 4) 'Run as Administrator' gives malware full access. An .exe file could install ransomware, keyloggers, or worse. Only open attachments from verified senders, and NEVER .exe files from email. Schedules should be PDFs or viewed in your school portal. When in doubt, don't open it - verify through official school channels."
}
```

---

Save all these files to `cybersafe/scenarios/`

That's all 15 scenarios complete!
