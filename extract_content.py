#!/usr/bin/env python3
"""
Extract player and scenario JSON files from markdown artifacts.
Usage: python extract_content.py content.md
"""

import re
import os
import sys
import json

def extract_json_blocks(markdown_text):
    """Extract all JSON blocks with their filenames and target directories from markdown."""
    # First, look for directory markers like: ## DIRECTORY: scenarios
    # Then match: ### filename.json followed by ```json ... ```
    
    files = []
    current_dir = None
    
    # Split by major headings to track directory context
    sections = re.split(r'\n##\s+', markdown_text)
    
    for section in sections:
        # Check if this section specifies a directory
        dir_match = re.match(r'(PHISHING|ONLINE SCAMS|IDENTITY THEFT|CYBERBULLYING|MALWARE|.*PERSONAS?)', section, re.IGNORECASE)
        
        if 'persona' in section.lower() or 'adversar' in section.lower():
            current_dir = 'players'
        elif any(x in section.lower() for x in ['phishing', 'scam', 'identity', 'bully', 'malware', 'scenario']):
            current_dir = 'scenarios'
        
        # Find all JSON blocks in this section
        pattern = r'###?\s+([a-z_]+\.json)\s*\n```json\s*\n(.*?)\n```'
        matches = re.findall(pattern, section, re.DOTALL)
        
        for filename, json_content in matches:
            try:
                # Validate JSON
                parsed = json.loads(json_content)
                
                # Determine directory from content if not set by heading
                if not current_dir:
                    if 'profession' in parsed and 'player' not in parsed:
                        current_dir = 'players'
                    elif 'category' in parsed and 'introduction' in parsed:
                        current_dir = 'scenarios'
                    else:
                        current_dir = '.'
                
                files.append((filename, json_content, current_dir))
                print(f"✓ Found valid JSON for {filename} -> {current_dir}/")
            except json.JSONDecodeError as e:
                print(f"✗ Invalid JSON in {filename}: {e}")
    
    return files

def save_files(files):
    """Save JSON files to their target directories."""
    saved_count = 0
    dirs_created = set()
    
    for filename, json_content, target_dir in files:
        # Create directory if needed
        if target_dir != '.' and target_dir not in dirs_created:
            os.makedirs(target_dir, exist_ok=True)
            print(f"📁 Created directory: {target_dir}/")
            dirs_created.add(target_dir)
        
        filepath = os.path.join(target_dir, filename)
        
        # Check if file exists
        if os.path.exists(filepath):
            response = input(f"⚠️  {filepath} already exists. Overwrite? (y/n): ")
            if response.lower() != 'y':
                print(f"Skipped {filename}")
                continue
        
        # Save file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json_content)
        
        print(f"💾 Saved {filepath}")
        saved_count += 1
    
    return saved_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_content.py <markdown_file>")
        print("\nOr paste content and press Ctrl+D:")
        markdown_text = sys.stdin.read()
    else:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            markdown_text = f.read()
    
    print("\n🔍 Extracting JSON files...\n")
    files = extract_json_blocks(markdown_text)
    
    if not files:
        print("❌ No valid JSON files found!")
        return
    
    # Group by directory for summary
    by_dir = {}
    for filename, _, target_dir in files:
        by_dir.setdefault(target_dir, []).append(filename)
    
    print(f"\n📦 Found {len(files)} files:\n")
    for dir_name, filenames in by_dir.items():
        print(f"  {dir_name}/: {len(filenames)} files")
    
    print()
    response = input("Proceed with extraction? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        return
    
    print()
    saved_count = save_files(files)
    
    print(f"\n✅ Successfully saved {saved_count}/{len(files)} files")
    print("\nRestart uvicorn to load the new content!")

if __name__ == "__main__":
    main()
