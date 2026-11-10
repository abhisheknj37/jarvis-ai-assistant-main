import os
import streamlit as st
from google import genai

st.set_page_config(page_title="JARVIS AI", page_icon="🤖", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: Inter, sans-serif; }
.stApp { background: radial-gradient(circle at 15% 5%, #172c50 0, #0b1220 38%, #070b14 100%); color: #edf3ff; }
.block-container { max-width: 980px; padding-top: 2.2rem; }
.hero { padding: 26px 28px; border: 1px solid #314565; border-radius: 22px; background: linear-gradient(120deg, #172b49, #101b31 65%, #15263e); margin-bottom: 22px; }
.hero h1 { margin: 0; font-size: 2.2rem; color: #f5f8ff; letter-spacing: -.04em; }
.hero p { color: #b8c8e3; margin: 8px 0 0; }
.stChatMessage { background: #121e31; border: 1px solid #263955; border-radius: 16px; }
.stChatInput textarea { background: #101a2a !important; color: white !important; }
div[data-testid="stButton"] button { border-radius: 12px; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🤖 JARVIS")
    st.caption("Personal AI assistant")
    st.markdown("---")
    st.markdown("**Powered by Google Gemini API**")
    st.caption("The hosted app supports text chat. Microphone, speaker and Windows desktop automation remain in the local desktop app.")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.caption("AI responses may be inaccurate. Verify important information.")

st.markdown("""
<div class="hero">
  <h1>🤖 JARVIS AI Assistant</h1>
  <p>Your intelligent assistant for questions, coding, ideas and everyday tasks.</p>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.warning("JARVIS needs a Gemini API key to reply. Add GEMINI_API_KEY in the Render service environment variables, then redeploy.")
    st.markdown("[Create a Gemini API key in Google AI Studio](https://aistudio.google.com/app/apikey)")
    st.info("Keep the key private. Add it directly in Render Dashboard → JARVIS service → Environment. Never paste it into GitHub or this chat.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Message JARVIS...", disabled=not bool(api_key))
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("JARVIS is thinking..."):
            try:
                client = genai.Client(api_key=api_key)
                history = st.session_state.messages[-12:]
                conversation = "\n".join(
                    f'{"User" if item["role"] == "user" else "JARVIS"}: {item["content"]}'
                    for item in history
                )
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=(
                        "You are JARVIS, a helpful, clear and friendly AI assistant. "
                        "Answer the latest user message and use recent conversation for context.\n\n"
                        + conversation
                    ),
                )
                answer = (response.text or "").strip()
                if not answer:
                    answer = "Gemini returned an empty response. Please try again."
            except Exception as exc:
                # Show Google's actual status/message so authentication, quota,
                # model and permission failures can be distinguished. Never show the key.
                detail = str(exc)
                if api_key:
                    detail = detail.replace(api_key, "[REDACTED]")
                detail = detail[:1200]
                answer = (
                    "JARVIS could not get a reply from Gemini. "
                    f"\n\n**{type(exc).__name__}:** {detail}\n\n"
                    "If this is 400/API_KEY_INVALID, recreate the key. "
                    "If 403, check API restrictions/project access. "
                    "If 429, check Gemini API quota and billing. "
                    "If 404, verify model availability for this project."
                )
            st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
