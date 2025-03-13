import time
import psutil
import win32gui
import win32process
from logger import log_event
from screenshot import take_screenshot
from config import TRACKED_APPS, last_window, running
from input_buffer_manager import flush_input_buffer

def get_active_window():
    """Return the active window's process name and window title."""
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        process_name = process.name()
        window_title = win32gui.GetWindowText(hwnd)
        return process_name, window_title
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return "Unknown", "Unknown"

def detect_switches():
    """Continuously monitor window/tab switches and log events immediately.
    
    Also flush the keyboard/mouse buffer if a switch occurs.
    """
    global last_window, running
    while running:
        process_name, window_title = get_active_window()
        if process_name != last_window["process_name"] or window_title != last_window["window_title"]:
            # Flush buffered input events when a process change is detected
            flush_input_buffer()
            event = "Tab switch" if process_name in TRACKED_APPS else "Window switch"
            log_event([event, process_name, window_title, "", "", "", "Suspicious activity detected", ""])
            take_screenshot(event)
            last_window["process_name"] = process_name
            last_window["window_title"] = window_title
        time.sleep(1)
