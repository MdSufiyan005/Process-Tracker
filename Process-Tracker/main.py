import time
from threading import Thread
from logger import log_event, init_csv
from window_monitor import detect_switches
from network_monitor import monitor_network
from input_monitor import on_key_press, on_key_release, on_click
from input_buffer_manager import flush_input_buffer
from pynput import keyboard, mouse
from config import running

def input_buffer_flush_thread():
    """Flush input events every 5 seconds."""
    while running:
        flush_input_buffer()
        time.sleep(5)

def start_monitoring():
    # Initialize CSV file
    init_csv()
    log_event(['Monitoring Started', "", "", "", "", "", "System initialized", ""])
    
    # Start threads for process and network monitoring
    threads = [
        Thread(target=detect_switches, daemon=True),
        Thread(target=monitor_network, daemon=True),
        Thread(target=input_buffer_flush_thread, daemon=True)
    ]
    for thread in threads:
        thread.start()
    
    # Start keyboard and mouse listeners for input events
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as key_listener, \
         mouse.Listener(on_click=on_click) as mouse_listener:
        key_listener.join()
        mouse_listener.join()
    
    # Log termination when listeners exit
    log_event(['Monitoring Stopped', "", "", "", "", "", "User terminated", ""])

if __name__ == '__main__':
    print("Starting student activity monitoring... (Press ESC to terminate)")
    print("Logging to CSV file: combined_activity_log.csv")
    start_monitoring()
