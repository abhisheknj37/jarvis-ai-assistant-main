try:
    import pywhatkit as pw
except ImportError:
    class _PyWhatKitStub:
        def playonyt(self, *args, **kwargs):
            print("pywhatkit not installed; cannot play music on YouTube")
    pw = _PyWhatKitStub()

def play_music_on_youtube(Song_name):
    pw.playonyt(Song_name)
