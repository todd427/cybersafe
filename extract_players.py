u#!/usr/bin/env python3
"""
Extract player and scenario JSON files from markdown artifacts.
Usage: python extract_content.py content.md
"""

import re
import os
import sys
import json

def extract_json_blocks(markdown_text, output_dir):
    """Extract all JSON blocks and their filenames from markdown."""
    # Pattern to match: ### filename.json OR ## filename.json followed by ```json ... ```
    pattern = r'###?\s+([a-z_]+\.json)\s*\n```json\s*\n(.*?)\n```'
    
    matches = re.findall(pattern, markdown_text, re.DOTALL | re.MULTILINE)
    
    files = []
    for filename, json_content in matches:
        try:
            # Validate JSON
            parsed = json.loads(json_content)
            files.append((filename, json_content))
            print(f"✓ Found valid JSON for {filename}")
        except json.JSONDecodeError as e:
            print(f"✗ Invalid JSON in {filename}: {e}")
    
    return files

def save_files(files, output_dir):
    """Save JSON files to directory."""
    os.makedirs(output_dir, exist_ok=True)
    
    saved_count = 0
    for filename, json_content in files:
        filepath = os.path.join(output_dir, filename)
        
        # Check if file exists
        if os.path.exists(filepath):
            response = input(f"⚠️  {filename} already exists. Overwrite? (y/n): ")
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
        print("Usage: python extract_content.py <markdown_file> [output_dir]")
        print("\nOr paste content and press Ctrl+D:")
        markdown_text = sys.stdin.read()
        output_dir = "."
    else:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    
    print("\n🔍 Extracting JSON files...\n")
    files = extract_json_blocks(markdown_text, output_dir)
    
    if not files:
        print("❌ No valid JSON files found!")
        return
    
    print(f"\n📦 Found {len(files)} files\n")
    
    # Determine directory based on content
    if files and any('player' in f[1] or 'profession' in f[1] for f in files[:3]):
        suggested_dir = "players"
    elif files and any('scenario' in f[1] or 'introduction' in f[1] for f in files[:3]):
        suggested_dir = "scenarios"
    else:
        suggested_dir = output_dir
    
    if output_dir == ".":
        response = input(f"Save to '{suggested_dir}/' directory? (y/n): ")
        if response.lower() == 'y':
            output_dir = suggested_dir
    
    saved_count = save_files(files, output_dir)
    
    print(f"\n✅ Successfully saved {saved_count}/{len(files)} files to {output_dir}/")

if __name__ == "__main__":
    main()
