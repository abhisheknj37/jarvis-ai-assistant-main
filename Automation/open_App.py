try:
    import pyautogui as gui
except ImportError:
    class _GuiStub:
        def __getattr__(self, name):
            def _missing(*args, **kwargs):
                print(f"pyautogui not installed; skipped {name}")
            return _missing
    gui = _GuiStub()

import subprocess
import time

def open_App(text):
    try:
       subprocess.run(text)
    except Exception as e:
        gui.press("win")
        time.sleep(0.2)
        gui.write(text)
        time.sleep(0.2)
        gui.press("enter")