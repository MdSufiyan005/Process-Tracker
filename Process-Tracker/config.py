import os

# Combined CSV setup
combined_log = "combined_activity_log.csv"
combined_headers = ['Timestamp', 'Event', 'Process Name', 'Window Title', 'PID', 'Local IP', 'Remote IP', 'Action Taken', 'Details']

# Screenshot folder setup
screenshot_folder = "screenshots"
os.makedirs(screenshot_folder, exist_ok=True)

# List of tracked applications
TRACKED_APPS = ['chrome.exe', 'msedge.exe', 'firefox.exe', 'code.exe', 'pycharm64.exe', 'notepad++.exe']

# Global flag for termination (modified at runtime)
running = True

# Store last active window details
last_window = {"process_name": "", "window_title": ""}

# Set to track seen network connections
seen_connections = set()
