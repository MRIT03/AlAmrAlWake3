import os
import django
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from scraper.models import Article

# Load .env
load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

# Init embedding + shared vector DB
embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key
)

vector_store = Chroma(
    persist_directory="../LLMProject/vector_db",
    embedding_function=embedding
)

# Prepare documents
docs = [
    Document(
        page_content=a.content,
        metadata={"title": a.title, "url": a.url, "source": a.source}
    )
    for a in Article.objects.all()
]

vector_store.add_documents(docs)

print(f"✅ Pushed {len(docs)} articles to ../LLMProject/vector_db")
