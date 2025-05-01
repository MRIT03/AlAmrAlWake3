import os
import django
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
import re

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

def should_index_article(url, content):
    homepage_prefixes = [
        "https://www.mtv.com.lb/",
        "https://www.lebanon24.com/",
        "https://www.otv.com.lb/",
        "https://www.lbcgroup.tv/",
        "https://www.almanar.com.lb/",
        "https://www.elnashra.com/",
        "https://www.annahar.com/",
        "https://www.nna-leb.gov.lb/",
        "https://www.aljazeera.com/"
    ]

    # EXCLUDE if exact homepage
    for homepage in homepage_prefixes:
        if url.rstrip("/").lower() == homepage.rstrip("/").lower():
            return False

    # EXCLUDE if content is too short
    if len(content.strip()) < 100:
        return False

    # INCLUDE if numeric ID present (5+ digits to avoid years like 2025)
    import re
    if re.search(r"\d{5,}", url):
        return True

    # INCLUDE if URL ends with a long-enough slug (indicates article)
    # Example: /news/president-calls-for-change
    slug = url.rstrip("/").split("/")[-1]
    if len(slug) > 10 and not slug.isdigit():
        return True

    return False

### NEW: Apply filter ###
docs = []
for a in Article.objects.all():
    url = a.url
    content = a.content

    if should_index_article(url, content):
        docs.append(
            Document(
                page_content=content,
                metadata={"title": a.title, "url": url, "source": a.source}
            )
        )
    else:
        print(f"Skipped: {url}")

vector_store.add_documents(docs)

print(f"Pushed {len(docs)} articles to ../LLMProject/vector_db")
