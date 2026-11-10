import streamlit as st
from llm4free import Client

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

@st.cache_resource
def get_jarvis_client():
    return Client()

with st.sidebar:
    st.markdown("## 🤖 JARVIS")
    st.caption("Personal AI chat")
    st.markdown("---")
    st.markdown("**Cloud assistant**")
    st.caption("Text chat is available here. Microphone, speaker and Windows desktop controls are supported only by the local desktop version.")
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
            answer = ""
            try:
                client = get_jarvis_client()
                history = st.session_state.messages[-12:]
                messages = [
                    {"role": "system", "content": "You are JARVIS, a helpful, clear and friendly AI assistant. Reply directly to the latest user message and use the conversation history for context."}
                ]
                messages.extend(
                    {"role": item["role"], "content": item["content"]}
                    for item in history
                )

                errors = []
                for model in ("auto", "Gemini/gemini-3.6-flash"):
                    try:
                        response = client.chat.completions.create(
                            model=model,
                            messages=messages,
                        )
                        answer = str(response.choices[0].message.content or "").strip()
                        if answer:
                            break
                        errors.append(f"{model}: empty response")
                    except Exception as exc:
                        errors.append(f"{model}: {type(exc).__name__}")

                if not answer:
                    answer = (
                        "I'm unable to reach an AI provider right now. "
                        "Please try again shortly. Provider checks: " + "; ".join(errors)
                    )
            except Exception as exc:
                answer = (
                    "JARVIS could not start its AI connection. "
                    f"Please retry in a moment. Error: {type(exc).__name__}"
                )

            st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
