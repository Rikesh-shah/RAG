# Medical Chatbot

A context-aware AI assistant powered by LangChain, Google Gemini, and a vector database. This app answers questions from PDF documents using Retrieval-Augmented Generation (RAG), with citations and memory across turns.

---

## 🧠 Features

- **PDF-powered chatbot** using LangChain's RAG architecture
- Uses LangChain RAG with `gemini` LLM (via `langchain_google_genai`)
- Embedding and retrieval using google embedding models + Chroma
- FastAPI backend with session-aware chat history
- Streamlit frontend with persistent memory per session
- Citations after each answer with document source tracking

---

## 🚀 Setup Instructions

### 1. Clone the Project


```bash
git clone https://github.com/yourname/azithro-rag-chatbot.git
cd azithro-rag-chatbot
```

### 2. Environment Setup

```bash
- uv init
- uv venv
- for windows
    .venv\Scripts\activate.bat
- for linux
    source .venv/bin/activate
- uv add -r requirements.txt
```

### 3. Run document ingestion
- python -m scripts.run_data_ingestion.py

### 4. Start Backend
- uvicorn backend.main:app --reload

### 5. Start Frontend
- Streamlit run frontend/streamlit_app.py
---

### to generate gemini api key:
    - Go to "https://aistudio.google.com/app/apikey"
    - Generate API Key
        - Click on "Generate API Key"
        - Copy the generated API key.
    and paste it in the .env file under GEMINI_API_KEY

---

### Summary

This project is a Retrieval-Augmented Generation (RAG) chatbot designed to answer medical questions based on PDF documents about Azithromycin. It’s built with a focus on clarity, modularity, and reliability, using technologies like LangChain for rag functionality, Google Gemini for LLM, FastAPI for backend, and Streamlit for frontend UI. The main reason behind choosing google chatmodels and enbedding models is because they provide high-quality embeddings and language generation capabilities which also provides better performance and free api key.

To handle the documents, we use langchain.document_loaders.PyPDFLoader to extract text from PDFs. The content is then broken down into meaningful chunks using RecursiveCharacterTextSplitter. These chunks are embedded using the googles **models/text-embedding-004** model and stored in a local Chroma vector database for fast and accurate similarity search.

The chatbot uses Google’s Gemini as its language model, integrated via langchain_google_genai.ChatGoogleGenerativeAI. Since Gemini doesn’t support system roles natively, we enable the convert_system_message_to_human flag to preserve important prompt instructions like "You are a helpful assistant." This setup also eliminates the need for a local GPU while still providing advanced language understanding.

On the backend, FastAPI powers two main endpoints: /start-session for initializing a new chat session and /ask for handling user queries. The system keeps track of chat history for each session, allowing for natural, multi-turn conversations. The frontend is built with Streamlit and features a clean, user-friendly interface, including a sidebar that displays past interactions.

To reduce hallucinations and improve factual accuracy, we use LangChain’s ConversationalRetrievalChain. This ensures the model only generates answers based on the relevant information retrieved from the documents. We also include clear instructions to stick to the context and cite sources inline, making the responses more trustworthy and traceable.