# from webscout import PhindSearch as brain


# ai = brain(
#     is_conversation=True,
#     max_tokens=800,
#     timeout=30,
#     intro='J.A.R.V.I.S',
#     filepath=r"C:\Users\chatu\Desktop\J.A.R.V.I.S\chat_hystory.txt",
#     update_file=True,
#     proxies={},
#     history_offset=10250,
#     act=None,
# )

# def Main_Brain(text):
#     r = ai.chat(text)
#     return r 

try:
    from webscout import PhindSearch
except ImportError:
    class PhindSearch:
        def __init__(self, *args, **kwargs):
            print("webscout not installed; using fallback brain stub")
        def chat(self, text):
            print("webscout unavailable; returning fallback response")
            return "I cannot access the AI search provider right now."

def Main_Brain(text):
    import os
    filepath = os.path.join(os.getcwd(), "chat_hystory.txt")
    ai = PhindSearch(quiet=True, filepath=filepath, is_conversation=None)

    res = ai.chat(text) # internel stream is not available for this Privider

    return res

