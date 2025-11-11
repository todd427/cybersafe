# Cyber Safer - File Installation Guide

## Files to Download from Artifacts

Click each artifact title above and copy the code, then save to these locations:

### 1. CSS
- **Artifact:** "css/styles.css"
- **Save to:** `cybersafe/static/css/styles.css`

### 2. JavaScript
- **Artifact:** "js/api.js"  
- **Save to:** `cybersafe/static/js/api.js`

### 3. HTML Pages
- **Artifact:** "index.html (Clean Welcome)"
- **Save to:** `cybersafe/static/index.html`

- **Artifact:** "categories.html"
- **Save to:** `cybersafe/static/categories.html`

- **Artifact:** "scenarios.html"
- **Save to:** `cybersafe/static/scenarios.html`

- **Artifact:** "scenario.html"
- **Save to:** `cybersafe/static/scenario.html`

- **Artifact:** "chat.html"
- **Save to:** `cybersafe/static/chat.html`

- **Artifact:** "results.html"
- **Save to:** `cybersafe/static/results.html`

## Quick Setup Commands

```bash
cd cybersafe/static
mkdir -p css js
# Then save each file as listed above
```

## After Saving All Files

```bash
cd cybersafe
uvicorn cybers:app --reload --port 8021
```

Then go to: http://localhost:8021

## Verification

Your `static/` folder should look like:
```
static/
├── index.html
├── categories.html
├── scenarios.html
├── scenario.html
├── chat.html
├── results.html
├── css/
│   └── styles.css
└── js/
    └── api.js
```
