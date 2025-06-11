import argparse
import json
import time
import logging

# --- Logging Setup ---
logging.basicConfig(filename='water_system.log', level=logging.INFO)



def log_change(parameter, old_value, new_value, user="system"):
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "parameter": parameter,
        "old_value": old_value,
        "new_value": new_value,
        "user": user
    }
    logging.info(json.dumps(log_entry))
 

# --- Simulated "current values" ---
current_ph = 7.0

# --- Argument Parser ---
parser = argparse.ArgumentParser(description="Water System Control CLI")
parser.add_argument("--set-ph", type=float, help="Set pH level")
parser.add_argument("--user", type=str, default="system", help="User making the change")

args = parser.parse_args()

# --- Perform Actions Based on Arguments ---
if args.set_ph is not None:
    old_value = current_ph
    new_value = args.set_ph
    current_ph = new_value
    print(f"pH changed from {old_value} to {new_value}")
    log_change("pH", old_value, new_value, args.user)
else:
    print("No changes made. Use --help for options.")
