import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.title("💊 Azithromycin RAG Chatbot")

if "session_id" not in st.session_state:
    res = requests.post(f"{BACKEND_URL}/start-session")
    st.session_state.session_id = res.json()["session_id"]
    st.session_state.chat_history = []

question = st.text_input("Ask a question from the documents:")

if st.button("Send") and question:
    payload = {
        "session_id": st.session_state.session_id,
        "question": question
    }
    res = requests.post(f"{BACKEND_URL}/ask", json=payload).json()
    
    st.session_state.chat_history = res["chat_history"]
    st.markdown(f"**Answer:** {res['answer']}")
    
    if res["sources"]:
        st.markdown(f"**Sources:** {', '.join(res['sources'])}")

if st.session_state.chat_history:
    st.subheader("Conversation History")
    for q, a in st.session_state.chat_history:
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Bot:** {a}")
