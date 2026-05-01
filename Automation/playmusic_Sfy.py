import webbrowser
try:
    import pyautogui as ui
except ImportError:
    class _GuiStub:
        def __getattr__(self, name):
            def _missing(*args, **kwargs):
                print(f"pyautogui not installed; skipped {name}")
            return _missing
    ui = _GuiStub()
import time

def play_music_on_spotify(song_name):
    webbrowser.open("https://open.spotify.com/")
    time.sleep(6)
    ui.hotkey("ctrl","shift","l")
    time.sleep(1)
    ui.write(song_name)
    time.sleep(3)
    ui.leftClick(805,515)
