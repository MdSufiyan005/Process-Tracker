import os
import time
import pyautogui
from logger import log_event
from config import screenshot_folder

def take_screenshot(reason):
    """
    Capture a screenshot, save it to the screenshots folder, and log the event.
    """
    timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
    filename = os.path.join(screenshot_folder, f'{reason}_{timestamp}.png')
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    log_event(['Screenshot Taken', "", "", "", "", "", "Screenshot saved", f"Screenshot saved: {filename}"])
