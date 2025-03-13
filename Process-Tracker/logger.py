import csv
import time
import os
from config import combined_log, combined_headers

def init_csv():
    """Initialize the CSV file with headers if it doesn't exist."""
    if not os.path.exists(combined_log):
        with open(combined_log, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(combined_headers)

def log_event(data, display=True):
    """
    Log an event to the CSV file.
    Data order: [Event, Process Name, Window Title, PID, Local IP, Remote IP, Action Taken, Details]
    """
    timestamp = time.strftime('%d-%m-%Y %H:%M:%S')
    row = [timestamp] + data
    with open(combined_log, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
    if display:
        print(f"[{timestamp}] {' | '.join(str(d) for d in data)}")
