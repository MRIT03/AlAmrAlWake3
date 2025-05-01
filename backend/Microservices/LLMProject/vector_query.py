# vector_query.py
import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env
load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

# Initialize embedding model
embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key
)

# Initialize vector DB
vector_store = Chroma(
    persist_directory="./vector_db",
    embedding_function=embedding
)

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-preview-04-17",
    google_api_key=api_key
)

def ask_articles(query):
    print(f"\n🔍 You asked: {query}")

    # Search vector DB
    docs = vector_store.similarity_search(query, k=3)

    print("\n📄 Relevant articles:\n")
    for i, doc in enumerate(docs, 1):
        print(f"{i}. {doc.metadata.get('title', 'No Title')}")
        print(f"   {doc.metadata.get('url', 'No URL')}\n")

    # Build prompt
    combined_content = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
Answer the following question using your own general knowledge. 
You may optionally use the following articles if they are helpful.

Question:
{query}

Articles:
{combined_content}
"""

    response = llm.invoke(prompt)

    print("\n🧠 Final Answer:\n")
    print(response.content)
