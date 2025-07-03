from langchain_community.vectorstores import Chroma
from rag.config import CHROMA_PATH, embedding_function

def create_vectorstore(chunks):
    return Chroma.from_documents(documents=chunks, embedding=embedding_function, persist_directory=CHROMA_PATH)

def load_vectorstore():
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)