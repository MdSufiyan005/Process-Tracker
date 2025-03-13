from pynput import keyboard, mouse
from window_monitor import get_active_window
from config import running
from input_buffer_manager import add_input_event

def on_key_press(key):
    """
    Add key press events to the input buffer.
    If the Esc key is pressed, also add a termination event and stop the listener.
    """
    global running
    process_name, window_title = get_active_window()
    event_data = ['Keypress', process_name, window_title, "", "", "", "Key pressed", str(key)]
    add_input_event(event_data)
    if key == keyboard.Key.esc:
        term_data = ['Termination requested', process_name, window_title, "", "", "", "Terminating", "Termination key pressed"]
        add_input_event(term_data)
        running = False
        return False  # Stop the keyboard listener

def on_key_release(key):
    pass

def on_click(x, y, button, pressed):
    """Add mouse click events to the input buffer."""
    global running
    if not running:
        return False
    action = "Pressed" if pressed else "Released"
    event_data = ['Mouse Click', "", "", "", "", "", f"Mouse {action}", f"({x}, {y})"]
    add_input_event(event_data)
