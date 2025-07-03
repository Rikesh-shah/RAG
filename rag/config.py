import os
import sys
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = "chroma_db"
EMBED_MODEL_NAME = "models/text-embedding-004"
PDF_DIR = "data/"

embedding_function = GoogleGenerativeAIEmbeddings(model=EMBED_MODEL_NAME)
