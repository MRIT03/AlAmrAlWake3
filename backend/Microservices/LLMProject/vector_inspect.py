from langchain_chroma import Chroma
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key
)

vector_store = Chroma(
    persist_directory="./vector_db",
    embedding_function=embedding
)

# List the metadata of all stored docs
docs = vector_store.similarity_search(" ", k=50)

print(f"Found {len(docs)} articles in vector DB.")
print("\nSample articles:")

for doc in docs:
    print(f"- {doc.metadata['title']}")
    print(f"  {doc.metadata['url']}\n")
