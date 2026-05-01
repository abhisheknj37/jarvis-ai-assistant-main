from ctypes import cast, POINTER
try:
    from comtypes import CLSCTX_ALL
except ImportError:
    CLSCTX_ALL = None
try:
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
except ImportError:
    AudioUtilities = None
    IAudioEndpointVolume = None
from TextToSpeech.Fast_DF_TTS import speak

# Function to get current volume
def get_volume_windows():
    if AudioUtilities is None or IAudioEndpointVolume is None or CLSCTX_ALL is None:
        speak("Audio control libraries are not installed; volume information is unavailable")
        return
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar() * 100
    speak(f"the device is running on {int(round(current_volume, 2))}  % volume level")

# Function to set the system volume
def set_volume_windows(percentage):
    if AudioUtilities is None or IAudioEndpointVolume is None or CLSCTX_ALL is None:
        speak("Audio control libraries are not installed; unable to set volume")
        return
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Convert percentage to scalar value (0.0 to 1.0)
    volume.SetMasterVolumeLevelScalar(percentage / 100, None)
    speak(f"Volume set to {percentage}%")

