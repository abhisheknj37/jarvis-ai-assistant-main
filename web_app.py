import uuid
from pathlib import Path

import streamlit as st
from webscout import PhindSearch

st.set_page_config(page_title="JARVIS AI Assistant", page_icon="🤖", layout="centered")
st.title("🤖 JARVIS AI Assistant")
st.caption("Cloud chat demo inspired by the original JARVIS project. Desktop controls, Windows automation, microphone and speaker features remain available only in the local Windows app.")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "jarvis" not in st.session_state:
    history = Path("/tmp") / f"jarvis-{uuid.uuid4().hex}.txt"
    try:
        st.session_state.jarvis = PhindSearch(
            quiet=True,
            filepath=str(history),
            is_conversation=True,
        )
    except Exception as exc:
        st.error(f"Could not initialize the AI provider: {exc}")
        st.stop()

for item in st.session_state.messages:
    with st.chat_message(item["role"]):
        st.markdown(item["content"])

prompt = st.chat_input("Ask JARVIS something...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("JARVIS is thinking..."):
            try:
                answer = st.session_state.jarvis.chat(prompt)
                answer = str(answer)
            except Exception as exc:
                answer = f"The AI provider is temporarily unavailable: {exc}"
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

if st.button("Clear this chat"):
    st.session_state.messages = []
    st.session_state.pop("jarvis", None)
    st.rerun()
