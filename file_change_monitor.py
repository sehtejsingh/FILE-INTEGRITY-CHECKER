import os
import hashlib
import json
import time

# Set the directory you want to monitor
MONITOR_DIR = "path/to/your/directory"  # Update this
HASH_RECORD_FILE = "file_hashes.json"

# Function to calculate SHA-256 hash of a file
def calculate_file_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

# Function to scan directory and return hash values
def scan_directory(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, directory)
            file_hashes[relative_path] = calculate_file_hash(full_path)
    return file_hashes

# Load previously saved hash values
def load_hashes():
    if os.path.exists(HASH_RECORD_FILE):
        with open(HASH_RECORD_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save current hash values
def save_hashes(hashes):
    with open(HASH_RECORD_FILE, 'w') as f:
        json.dump(hashes, f, indent=4)

# Detect added, removed, or modified files
def detect_changes(old_hashes, new_hashes):
    old_files = set(old_hashes.keys())
    new_files = set(new_hashes.keys())

    added = new_files - old_files
    removed = old_files - new_files
    modified = {file for file in old_files & new_files if old_hashes[file] != new_hashes[file]}

    return added, removed, modified

# Main function to run monitoring once
def monitor_once():
    print("Scanning directory for file changes...")
    old_hashes = load_hashes()
    new_hashes = scan_directory(MONITOR_DIR)

    added, removed, modified = detect_changes(old_hashes, new_hashes)

    print("\n=== File Changes Detected ===")
    if added:
        print("Added Files:")
        for file in added:
            print(f" + {file}")
    if removed:
        print("Removed Files:")
        for file in removed:
            print(f" - {file}")
    if modified:
        print("Modified Files:")
        for file in modified:
            print(f" * {file}")
    if not (added or removed or modified):
        print("No changes detected.")

    save_hashes(new_hashes)

if __name__ == "__main__":
    monitor_once()
