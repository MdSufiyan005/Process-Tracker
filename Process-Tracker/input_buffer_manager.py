import threading
from logger import log_event

input_buffer = []
buffer_lock = threading.Lock()

def add_input_event(event_data):
    """Add a keyboard/mouse event (a list) to the buffer."""
    with buffer_lock:
        input_buffer.append(event_data)

def flush_input_buffer():
    """Flush and log all pending input events from the buffer."""
    with buffer_lock:
        while input_buffer:
            event_data = input_buffer.pop(0)
            log_event(event_data)
