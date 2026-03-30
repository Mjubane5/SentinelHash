import hashlib
import time
import os

# 1. Define the file we are protecting
TARGET_FILE = "target_file.txt"

def calculate_sha256(filepath):
    """Generates a SHA-256 hash for a given file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        # Read the file in chunks to handle large files efficiently
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def start_monitoring():
    print(f"[*] SentinelHash Initializing...")
    
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Error: {TARGET_FILE} not found.")
        return

    # 2. Calculate the baseline fingerprint
    baseline_hash = calculate_sha256(TARGET_FILE)
    print(f"[*] Baseline Hash: {baseline_hash}")
    print(f"[*] Monitoring {TARGET_FILE} for changes. Press Ctrl+C to stop.\n")

    # 3. Enter the continuous monitoring loop
    try:
        while True:
            time.sleep(2) # Pause for 2 seconds to save CPU power
            current_hash = calculate_sha256(TARGET_FILE)
            
            if current_hash != baseline_hash:
                print(f"[CRITICAL ALERT] FILE MODIFIED AT {time.ctime()}!")
                print(f"[-] Old Hash: {baseline_hash}")
                print(f"[+] New Hash: {current_hash}")
                
                # Update baseline so it doesn't spam the console forever
                baseline_hash = current_hash 
                print("\n[*] Baseline updated. Resuming monitoring...\n")
                
    except KeyboardInterrupt:
        print("\n[*] SentinelHash shut down securely.")

if __name__ == "__main__":
    start_monitoring()
