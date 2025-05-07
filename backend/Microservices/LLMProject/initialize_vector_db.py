# initialize_vector_db.py

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_GEMINI_API_KEY not found in environment variables.")

# Initialize embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key
)

# Initialize Chroma (empty or persistent)
vector_store = Chroma(
    collection_name="embeddings",
    embedding_function=embeddings,
    persist_directory="./vector_db",
    collection_metadata={"hnsw:space": "cosine"}
)

print("✅ Vector database initialized (empty or existing).")
