import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key
)

vector_store = Chroma(
    persist_directory="./vector_db",
    embedding_function=embedding
)

def search_articles(query, k=3):
    docs = vector_store.similarity_search(query, k=k)
    return docs
