# …\Microservices\LLMProject\index_articles.py
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# ───────────────────────────────────────────────────────────
# 1) locate Scrape service root (folder that has manage.py)
# ───────────────────────────────────────────────────────────
DJANGO_PROJECT_ROOT = (Path(__file__).resolve().parent.parent / "Scrape").resolve()
if not (DJANGO_PROJECT_ROOT / "manage.py").exists():
    raise FileNotFoundError(f"manage.py not found under {DJANGO_PROJECT_ROOT}")

# make the root importable so we can import `config`, `scraper`, …
sys.path.insert(0, str(DJANGO_PROJECT_ROOT))

# ───────────────────────────────────────────────────────────
# 2) choose the right settings module
# ───────────────────────────────────────────────────────────
if (DJANGO_PROJECT_ROOT / "config" / "settings.py").exists():
    SETTINGS_MODULE = "config.settings"               # ← YOUR CASE
elif (DJANGO_PROJECT_ROOT / "Scrape" / "config" / "settings.py").exists():
    SETTINGS_MODULE = "Scrape.config.settings"
elif (DJANGO_PROJECT_ROOT / "Scrape" / "settings.py").exists():
    SETTINGS_MODULE = "Scrape.settings"
elif (DJANGO_PROJECT_ROOT / "settings.py").exists():
    SETTINGS_MODULE = "settings"
else:
    raise FileNotFoundError("Couldn't locate a Django settings.py")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)

# ───────────────────────────────────────────────────────────
# 3) bootstrap Django
# ───────────────────────────────────────────────────────────
import django                                  # noqa: E402
django.setup()

# ───────────────────────────────────────────────────────────
# 4) import models + LangChain bits
# ───────────────────────────────────────────────────────────
from scraper.models import Article             # noqa: E402
from langchain_chroma import Chroma            # noqa: E402
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # noqa: E402
from langchain_core.documents import Document  # noqa: E402

# ───────────────────────────────────────────────────────────
# 5) load env vars
# ───────────────────────────────────────────────────────────
load_dotenv(DJANGO_PROJECT_ROOT / ".env")
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GOOGLE_GEMINI_API_KEY not set")

# ───────────────────────────────────────────────────────────
# 6) helpers
# ───────────────────────────────────────────────────────────
def get_articles_from_db():
    docs = []
    for a in Article.objects.all():
        docs.append(
            {
                "title": a.title,
                "content": a.content,
                "url": a.url,
                "source": a.source,
                "date": a.date_scraped.strftime("%Y-%m-%d") if a.date_scraped else "unknown",
            }
        )
    return docs


def index_articles():
    raw_articles = get_articles_from_db()
    if not raw_articles:
        print("⚠️  No articles found in DB – nothing to index.")
        return

    docs = [
        Document(
            page_content=art["content"],
            metadata={
                "title": art["title"],
                "url": art["url"],
                "source": art["source"],
                "date": art["date"],
            },
        )
        for art in raw_articles
    ]

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key,
    )

    VECTOR_DB_PATH = (Path(__file__).resolve().parent / "vector_db").resolve()
    VECTOR_DB_PATH.mkdir(exist_ok=True)

    Chroma.from_documents(
        docs,
        embeddings,
        collection_name="news_articles",
        persist_directory=str(VECTOR_DB_PATH),
    ).persist()

    print(f"✅  {len(docs)} articles indexed into {VECTOR_DB_PATH}")


# ───────────────────────────────────────────────────────────
# 7) run it
# ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    index_articles()
