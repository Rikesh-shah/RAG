# 💊 Azithromycin RAG Chatbot

A context-aware AI assistant powered by LangChain, Google Gemini Pro (`ChatGoogleGenerativeAI`), and a vector database. This app answers questions from PDF documents using Retrieval-Augmented Generation (RAG), with citations and memory across turns.

---

## 🧠 Features

- Uses LangChain RAG with `gemini-pro` LLM (via `langchain_google_genai`)
- Embedding and retrieval using `all-MiniLM-L6-v2` + Chroma
- FastAPI backend with session-aware chat history
- Streamlit frontend with persistent memory per session
- Citations after each answer with document source tracking

---

## 🚀 Setup Instructions

### 1. Clone and Setup

```bash
git clone https://github.com/yourname/azithro-rag-chatbot.git
cd azithro-rag-chatbot
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate
pip install -r requirements.txt
