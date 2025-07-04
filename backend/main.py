from fastapi import FastAPI, Request
from uuid import uuid4
from pydantic import BaseModel
from rag import build_chain

app = FastAPI()
chain = build_chain()
sessions = {}

class AskRequest(BaseModel):
    session_id: str
    question: str

@app.post("/start-session")
def start_session():
    session_id = str(uuid4())
    sessions[session_id] = []
    return {"session_id": session_id}

@app.post("/ask")
def ask(req: AskRequest):
    chat_history = sessions.get(req.session_id, [])
    result = chain({"question": req.question, "chat_history": chat_history})
    sessions[req.session_id].append((req.question, result["answer"]))
    
    sources = set()
    for doc in result.get("source_documents", []):
        # sources.add(doc.metadata.get("source", "Unknown"))
        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "N/A")
        sources.add(f"{source} (Page {page})")
    return {
        "answer": result["answer"],
        "sources": list(sources),
        "chat_history": sessions[req.session_id]
    }
