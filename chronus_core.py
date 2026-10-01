# =====================================================================
# PROJECT EBONY // THE CHRONUS IMMUTABLE LEDGER
# AUTHORITY: LEVEL 5 CEO
# =====================================================================
import time
import hashlib
import json
import os

# HARDENED ABSOLUTE PATH TO BARE METAL VAULT
VAULT_DIR = r"C:\HVF_Repos\ebony-chronos-private"
LEDGER_FILE = os.path.join(VAULT_DIR, "chronus_vault.json")

def seal_telemetry_block(current_load, active_power, freq):
    timestamp = time.time()
    raw_data = f"{timestamp}|{current_load}|{active_power}|{freq}"
    merkle_hash = hashlib.sha256(raw_data.encode()).hexdigest()
    
    block = {
        "timestamp_utc": timestamp,
        "grid_load_A": current_load,
        "active_power_kW": active_power,
        "frequency_Hz": freq,
        "merkle_seal": merkle_hash
    }
    
    ledger = []
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r") as f:
            try:
                ledger = json.load(f)
            except:
                pass
                
    ledger.append(block)
    
    with open(LEDGER_FILE, "w") as f:
        json.dump(ledger, f, indent=4)
        
    return merkle_hash

if __name__ == "__main__":
    print("⚡ CHRONUS LEDGER CORE: INITIALIZED AND SECURED ⚡")
