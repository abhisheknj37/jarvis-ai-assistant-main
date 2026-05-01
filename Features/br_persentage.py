try:
    import wmi
except ImportError:
    wmi = None
from TextToSpeech.Fast_DF_TTS import speak
def get_brightness_windows():
    if wmi is None:
        return "wmi not installed; brightness unavailable"
    try:
        w = wmi.WMI(namespace='wmi')
        brightness_methods = w.WmiMonitorBrightness()
        brightness_percentage = brightness_methods[0].CurrentBrightness
        return brightness_percentage
    except Exception as e:
        return f"Error: {e}"

def check_br_persentage():
    brightness = get_brightness_windows()
    speak(f"Current Brightness: {brightness}%")

