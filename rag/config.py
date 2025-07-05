import os
import sys
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = "chroma_db"
EMBED_MODEL_NAME = "models/text-embedding-004"
PDF_DIR = "data/"

# embedding function for enbedding creation of docs
# embedding_function = GoogleGenerativeAIEmbeddings(model=EMBED_MODEL_NAME)
embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
