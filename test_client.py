#!/usr/bin/env python3
"""
Simple test client to verify the Cyber Safer server is running and responding.

Usage:
  python test_client.py                    # Test health endpoint
  python test_client.py test               # Test model generation
  python test_client.py chat "Hello!"      # Test chat with custom message
"""

import sys
import requests
import json
from time import time

BASE_URL = "http://localhost:8021"

def test_health():
    """Test the health check endpoint."""
    print("🏥 Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Server is running: {data}")
            return True
        else:
            print(f"❌ Server returned {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Is it running?")
        print("💡 Start it with: uvicorn cybers:app --reload --port 8021")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_model_endpoint():
    """Test the model generation endpoint."""
    print("\n🤖 Testing model endpoint...")
    print("⏳ This may take 10-30 seconds for first generation...")
    
    try:
        start = time()
        response = requests.get(f"{BASE_URL}/api/test", timeout=60)
        elapsed = time() - start
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Model test passed in {elapsed:.1f}s")
            print(f"   Model: {data.get('model')}")
            print(f"   Device: {data.get('device')}")
            print(f"   Response: {data.get('response')}")
            return True
        else:
            print(f"❌ Test failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except requests.exceptions.Timeout:
        print("❌ Request timed out after 60 seconds")
        print("💡 Model might be loading slowly or hung")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_chat(message="Hello! Can you hear me?"):
    """Test streaming chat endpoint."""
    print(f"\n💬 Testing chat with message: '{message}'")
    print("⏳ Waiting for response...")
    
    try:
        start = time()
        response = requests.post(
            f"{BASE_URL}/api/chat/stream",
            json={"message": message},
            stream=True,
            timeout=60
        )
        
        if response.status_code == 200:
            print("📝 Response: ", end="", flush=True)
            full_response = ""
            for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
                if chunk:
                    print(chunk, end="", flush=True)
                    full_response += chunk
            
            elapsed = time() - start
            print(f"\n\n✅ Chat test passed in {elapsed:.1f}s")
            print(f"   Response length: {len(full_response)} characters")
            return True
        else:
            print(f"❌ Chat failed with status {response.status_code}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Request timed out after 60 seconds")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_scenarios():
    """Test scenarios endpoint."""
    print("\n📚 Testing scenarios endpoint...")
    
    try:
        response = requests.get(f"{BASE_URL}/api/scenarios", timeout=10)
        if response.status_code == 200:
            data = response.json()
            categories = data.get('categories', {})
            total = sum(len(scenarios) for scenarios in categories.values())
            print(f"✅ Found {total} scenarios in {len(categories)} categories")
            for cat, scenarios in categories.items():
                print(f"   {cat}: {len(scenarios)} scenarios")
            return True
        else:
            print(f"❌ Failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run tests based on command line arguments."""
    print("=" * 60)
    print("🛡️  CYBER SAFER - SERVER TEST CLIENT")
    print("=" * 60)
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "test":
            # Full test
            if not test_health():
                sys.exit(1)
            if not test_model_endpoint():
                sys.exit(1)
            sys.exit(0)
            
        elif command == "chat":
            message = sys.argv[2] if len(sys.argv) > 2 else "Hello! Can you hear me?"
            if not test_health():
                sys.exit(1)
            if not test_chat(message):
                sys.exit(1)
            sys.exit(0)
            
        elif command == "scenarios":
            if not test_health():
                sys.exit(1)
            if not test_scenarios():
                sys.exit(1)
            sys.exit(0)
            
        else:
            print(f"Unknown command: {command}")
            print("\nUsage:")
            print("  python test_client.py              # Test health")
            print("  python test_client.py test         # Test model")
            print("  python test_client.py chat [msg]   # Test chat")
            print("  python test_client.py scenarios    # Test scenarios")
            sys.exit(1)
    
    # Default: just test health
    if test_health():
        print("\n💡 Server is running! Try:")
        print("   python test_client.py test         # Test model generation")
        print("   python test_client.py chat         # Test chat")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
