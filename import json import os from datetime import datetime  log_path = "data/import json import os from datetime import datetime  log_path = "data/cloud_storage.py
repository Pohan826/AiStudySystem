import json
import os
from datetime import datetime

log_path = "data/logs.json"

def save_focus_log(is_focused):
    now = datetime.now().isoformat(timespec='seconds')
    entry = {"time": now, "focused": is_focused}

    if not os.path.exists(log_path):
        with open(log_path, 'w') as f:
            json.dump([], f)

    with open(log_path, 'r') as f:
        data = json.load(f)

    data.append(entry)

    with open(log_path, 'w') as f:
        json.dump(data, f, indent=2)
