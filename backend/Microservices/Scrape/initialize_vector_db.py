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

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

# Set up embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", 
    google_api_key=api_key
)

# Build documents from DB
documents = []
for article in Article.objects.all():
    documents.append(
        Document(
            page_content=article.content,
            metadata={
                "title": article.title,
                "url": article.url,
                "source": article.source,
                "date": str(article.date_scraped),
            }
        )
    )

# Initialize vector store
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="../LLMProject/vector_db"
)

print(f"Indexed {len(documents)} articles into Chroma vector DB.")
