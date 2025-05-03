import os
import django
import chromadb
from sentence_transformers import SentenceTransformer
from django.conf import settings

# --- Django setup ---
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Scrape.config.settings')
django.setup()

from scraper.models import Article

# --- Initialize Chroma ---
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="articles")

# --- Load Sentence Transformer ---
model = SentenceTransformer('all-MiniLM-L6-v2')

# --- Fetch articles ---
articles = Article.objects.all()

# --- Prepare data ---
documents = []
metadatas = []
ids = []

for article in articles:
    if article.content and article.content.strip():  # Skip empty content
        doc_text = article.title + ". " + article.content
        documents.append(doc_text)
        metadatas.append({
            "title": article.title,
            "url": article.url,
            "source": article.source
        })
        ids.append(str(article.id))  # IDs must be strings

# --- Vectorize and insert ---
if documents:
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    print(f"Indexed {len(documents)} articles into Chroma.")
else:
    print("No articles with content found.")
