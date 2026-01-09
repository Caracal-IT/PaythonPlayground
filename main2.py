import os
import sys
import time
import threading

import hashlib

def file_hash(filename: str):
    try:
        with open(filename, "rb") as f:
            file_bytes = f.read()

            return hashlib.sha256(file_bytes).hexdigest()
    except FileNotFoundError:
        return None

def watch_file():
    """Native polling monitor."""
    #last_mtime = os.path.getmtime(filename) if os.path.exists(filename) else 0

    filename = "settings2.json"
    last_mtime = os.path.getmtime(filename) if os.path.exists(filename) else 0

    #print("Testing", last_mtime)
    #print(file_hash(filename))

    while True:
        if os.path.exists(filename):
            current_mtime = os.path.getmtime(filename)
            if current_mtime != last_mtime:
                last_mtime = current_mtime
                print(f"{filename} has changed, reloading settings...")
        time.sleep(2)  # Check every 2 seconds

t = threading.Thread(target=watch_file, daemon=True)
t.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down...")
    sys.exit(0)
