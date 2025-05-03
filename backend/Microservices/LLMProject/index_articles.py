# index_articles.py

import os
import django
from dotenv import load_dotenv
import sys
sys.path.append("C:/Users/User/Desktop/AlAmrAlWake3/backend/Microservices/Scrape")

# --- Django Setup ---
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Scrape.config.settings')  # Change Scrape.config if needed
django.setup()

from scraper.models import Article
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

# --- Get Articles ---
def get_articles_from_db():
    articles = Article.objects.all()
    docs = []
    for article in articles:
        docs.append({
            "title": article.title,
            "content": article.content,
            "url": article.url,
            "source": article.source,
            "date": article.date_scraped.strftime("%Y-%m-%d") if article.date_scraped else "unknown"
        })
    return docs

# --- Index to Chroma ---
def index_articles():
    articles = get_articles_from_db()
    documents = [
        Document(
            page_content=art["content"],
            metadata={"title": art["title"], "url": art["url"], "source": art["source"], "date": art["date"]}
        ) for art in articles
    ]

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )

    vector_store = Chroma.from_documents(
        documents,
        embeddings,
        persist_directory="./vector_db"
    )

    print("✅ Articles indexed into ChromaDB successfully.")

if __name__ == "__main__":
    index_articles()
