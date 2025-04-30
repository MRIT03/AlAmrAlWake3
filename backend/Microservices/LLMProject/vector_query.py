import os
import django
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

# Load keys
load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

# Init embeddings + vector DB
embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key
)

vector_store = Chroma(
    persist_directory="./vector_db",
    embedding_function=embedding
)

# LLM for summarizing
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=api_key
)

def ask_articles(query):
    print(f"\n🔍 You asked: {query}")
    
    # Search vector DB
    docs = vector_store.similarity_search(query, k=3)

    print("\n📄 Relevant articles:\n")
    for i, doc in enumerate(docs, 1):
        print(f"{i}. {doc.metadata['title']}")
        print(f"   {doc.metadata['url']}\n")

    # Summarize findings
    combined_content = "\n\n".join(d.page_content for d in docs)
    prompt = f"Based on the following articles, answer the question:\n\n{query}\n\nArticles:\n{combined_content}"

    response = llm.invoke(prompt)
    
    print("\nSummary:\n")
    print(response.content)
