import os
import django
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# ---------------- Django setup ----------------
load_dotenv()

# --- Adjust these paths ---
DJANGO_PROJECT_PATH = "../Scrape"  # Update if needed
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from scraper.models import Article

# ---------------- Vector DB setup ----------------
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_GEMINI_API_KEY not found in environment variables.")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key
)

vector_store = Chroma(
    collection_name="embeddings",
    embedding_function=embeddings,
    persist_directory="./vector_db",
    collection_metadata={"hnsw:space": "cosine"}
)

# ---------------- Pull from DB ----------------
# Get already indexed URLs from Chroma metadata
existing = vector_store.get(include=["metadatas"])

indexed_urls = set()
for meta in existing['metadatas']:
    if meta and 'url' in meta:
        indexed_urls.add(meta['url'])
        
articles = Article.objects.all()
new_documents = []
for article in articles:
    if article.url in indexed_urls:
        continue  # Skip duplicates

    content = article.content.strip()
    title = article.title
    url = article.url
    source = article.source
    date = article.date_scraped.strftime("%Y-%m-%d") if article.date_scraped else "Unknown"

    doc = Document(
        page_content=content,
        metadata={
            "title": title,
            "url": url,
            "source": source,
            "date": date
        }
    )
    new_documents.append(doc)

if new_documents:
    vector_store.add_documents(new_documents)
    print(f"✅ {len(new_documents)} new articles added to Chroma.")
else:
    print("✅ No new articles to add.")