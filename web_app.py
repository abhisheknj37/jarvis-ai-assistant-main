import streamlit as st
from llm4free.client import Client

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
    st.caption("Personal AI chat")
    st.markdown("---")
    st.markdown("**Cloud demo**")
    st.caption("This version provides AI chat in your browser. Windows automation, microphone, speaker and desktop controls remain in the local Windows app.")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.caption("AI responses can be inaccurate. Verify important information.")

st.markdown("""
<div class="hero">
  <h1>🤖 JARVIS AI Assistant</h1>
  <p>Your intelligent assistant for questions, coding, ideas and everyday tasks.</p>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "provider" not in st.session_state:
    try:
        st.session_state.provider = Client()
        st.session_state.provider_error = ""
    except Exception as exc:
        st.session_state.provider = None
        st.session_state.provider_error = str(exc)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Message JARVIS...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("JARVIS is thinking..."):
            try:
                if st.session_state.provider is None:
                    st.session_state.provider = Meta()
                context = st.session_state.messages[-12:]
                conversation = "\n".join(
                    f'{"User" if item["role"] == "user" else "JARVIS"}: {item["content"]}'
                    for item in context
                )
                response = st.session_state.provider.chat.completions.create(
                    model="auto",
                    messages=[
                        {"role": "system", "content": "You are JARVIS, a helpful, clear and friendly AI assistant. Give accurate, practical answers."},
                        {"role": "user", "content": conversation},
                    ],
                )
                answer = str(response.choices[0].message.content or "").strip()
                if not answer:
                    answer = "I couldn't generate a response. Please try again."
            except Exception as exc:
                answer = (
                    "The AI provider is temporarily unavailable. Please try again in a moment. "
                    f"Technical detail: {exc}"
                )
            st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
