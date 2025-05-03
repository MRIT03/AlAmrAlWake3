"""
Call from a cron / Django‑Q / Celery beat task every X minutes.
Adds only *new* qualifying articles.
"""
import os, django, re, hashlib
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from scraper.models import Article

# ---------------------------------------------------------------------------
load_dotenv()
emb_fn = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.environ["GOOGLE_GEMINI_API_KEY"],
)

VDB_DIR = os.path.join(os.path.dirname(__file__), "vector_db")
vstore = Chroma(persist_directory=VDB_DIR, embedding_function=emb_fn)

# ---------------------------------------------------------------------------
def article_fingerprint(article) -> str:
    """A stable hash so we don't double‑index an identical item."""
    raw = f"{article.pk}:{hashlib.md5(article.content.encode()).hexdigest()}"
    return raw

already = {m["id"] for m in vstore.get(include=["metadatas"])["metadatas"]}

adds = []
for a in Article.objects.exclude(pk__in=already):
    if len(a.content or "") < 100:
        continue                                      # skip boilerplate
    if re.fullmatch(r"https?://[^/]+/?", a.url.strip("/")):
        continue                                      # skip home pages
    adds.append(
        Document(
            page_content=a.content,
            metadata={
                "id": a.pk,
                "title": a.title,
                "url": a.url,
                "source": a.source,
                "date": a.date_scraped.isoformat(),
                "_fingerprint": article_fingerprint(a),
            },
        )
    )

if adds:
    vstore.add_documents(adds)
print(f"Pushed {len(adds)} new articles to vector DB")
