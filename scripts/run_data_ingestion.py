import os
import sys
from rag import load_and_split_pdfs, create_vectorstore, PDF_DIR

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_data_ingestion():
    docs = load_and_split_pdfs(PDF_DIR)
    db = create_vectorstore(docs)
    db.persist()

if __name__ == "__main__":
    run_data_ingestion()