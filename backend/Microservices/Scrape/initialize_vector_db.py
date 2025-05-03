"""
Run once (or whenever you want a clean rebuild)  

$ python manage.py shell < initialize_vector_db.py
"""
import os, django
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# --- Django -----------------------------------------------------------------
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from scraper.models import Article

# --- Env & embeddings -------------------------------------------------------
load_dotenv()
emb_fn = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.environ["GOOGLE_GEMINI_API_KEY"],
)

VDB_DIR = os.path.join(os.path.dirname(__file__), "../LLMProject/vector_db")

# --- Index every article ----------------------------------------------------
docs = [
    Document(
        page_content=a.content,
        metadata={
            "id": a.pk,
            "title": a.title,
            "url": a.url,
            "source": a.source,          # e.g. “MTV Lebanon”
            "date": a.date_scraped.isoformat(),
        },
    )
    for a in Article.objects.exclude(content__isnull=True).exclude(content__exact="")
]

Chroma.from_documents(docs, emb_fn, persist_directory=VDB_DIR)
print(f"Indexed {len(docs)} articles → {VDB_DIR}")
