import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Azithromycin RAG Chatbot", layout="wide")
st.title("💊 Azithromycin RAG Chatbot")

# Sidebar for session & chat history
with st.sidebar:
    st.header("Chat History")
    
    if "session_id" not in st.session_state:
        res = requests.post(f"{BACKEND_URL}/start-session")
        st.session_state.session_id = res.json()["session_id"]
        st.session_state.chat_history = []

    if st.session_state.chat_history:
        for i, turn in enumerate(st.session_state.chat_history):
            st.markdown(f"**Q{i+1}:** {turn[0][:50]}...")

    if st.button("Start New Session"):
        res = requests.post(f"{BACKEND_URL}/start-session")
        st.session_state.session_id = res.json()["session_id"]
        st.session_state.chat_history = []
        st.rerun()

# main chat UI
st.subheader("📥 Ask your medical question:")
question = st.text_input("Type your question here...")

if st.button("Ask"):
    if question:
        payload = {
            "session_id": st.session_state.session_id,
            "question": question
        }
        with st.spinner("Generating answer..."):
            res = requests.post(f"{BACKEND_URL}/ask", json=payload).json()
            st.session_state.chat_history = res["chat_history"]
            answer = res["answer"]
            sources = res["sources"]

        # showing the reponse along with sources
        st.markdown(f"**🤖 Assistant:** {answer}")
        if sources:
            st.markdown("**📚 Sources:**")
            for s in sources:
                st.markdown(f"- {s}")
    else:
        st.warning("Please enter a question before clicking Ask.")

# to view the full conversation of a single session.
with st.expander("Full Conversation"):
    for q, a in st.session_state.chat_history:
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Bot:** {a}")
