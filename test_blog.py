import json
import os
import sys

# --- Configuration ---
POSTS_FILE = 'posts.json'
INDEX_FILE = 'index.html'
TARGET_STRING = 'tailwindcss'

def check_json_validity(filepath):
    """Checks if the provided file is valid JSON."""
    print(f"--- 1. Checking JSON validity of {filepath} ---")
    if not os.path.exists(filepath):
        print(f"[FAILURE] Error: File {filepath} not found.")
        return False, "File not found."

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # We load the whole file to check structure, assuming it's a single JSON object/array.
            json_data = json.load(f)
        print("[SUCCESS] posts.json is valid JSON.")
        return True, "Valid."
    except json.JSONDecodeError as e:
        print(f"[FAILURE] Error: {filepath} contains invalid JSON.")
        print(f"         Details: {e}")
        return False, f"Invalid JSON structure: {e}"
    except Exception as e:
        print(f"[FAILURE] An unexpected error occurred reading {filepath}: {e}")
        return False, str(e)

def check_string_presence(filepath, target):
    """Checks if the specified string is present in the HTML file."""
    print(f"\n--- 2. Checking for '{target}' presence in {filepath} ---")
    if not os.path.exists(filepath):
        print(f"[FAILURE] Error: File {filepath} not found.")
        return False, "File not found."

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if target in content:
            print(f"[SUCCESS] Found the string '{target}' in {filepath}.")
            return True, "Found."
        else:
            print(f"[FAILURE] String '{target}' was NOT found in {filepath}.")
            return False, "Not found."
    except Exception as e:
        print(f"[FAILURE] An unexpected error occurred reading {filepath}: {e}")
        return False, str(e)

def main():
    """Runs all validation checks and summarizes results."""
    overall_success = True
    results = []

    # Check JSON
    json_ok, json_message = check_json_validity(POSTS_FILE)
    results.append({"check": "JSON Validation", "passed": json_ok, "detail": json_message})
    if not json_ok:
        overall_success = False

    # Check String Presence
    string_ok, string_message = check_string_presence(INDEX_FILE, TARGET_STRING)
    results.append({"check": "HTML Content Validation", "passed": string_ok, "detail": string_message})
    if not string_ok:
        overall_success = False

    print("\n" + "="*50)
    if overall_success:
        print("✅ TEST SUITE PASSED: All validations succeeded!")
    else:
        print("❌ TEST SUITE FAILED: One or more critical checks failed.")
    print("="*50)

if __name__ == "__main__":
    main()