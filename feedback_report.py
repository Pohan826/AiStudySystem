import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter
from ace_tools import display_dataframe_to_user

log_path = "data/logs.json"

with open(log_path, 'r') as f:
    logs = json.load(f)

df = pd.DataFrame(logs)

df["time"] = pd.to_datetime(df["time"])
df["date"] = df["time"].dt.date
df["hour"] = df["time"].dt.hour
df["minute"] = df["time"].dt.minute
df["focused"] = df["focused"].astype(bool)

daily_focus = df[df["focused"]].groupby("date").size() * 0.5

plt.figure(figsize=(10, 5))
daily_focus.plot(kind="bar", color="skyblue")
plt.title("Daily Focus Time (minutes)")
plt.xlabel("Date")
plt.ylabel("Focus Time (min)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

display_dataframe_to_user("Daily Focus Records", df[["time", "focused"]])
