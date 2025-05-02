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
    docs = vector_store.similarity_search(query, k=5)

    # Remove duplicate URLs
    unique_docs = {}
    for doc in docs:
        url = doc.metadata.get('url', 'no-url')
        if url not in unique_docs:
            unique_docs[url] = doc

    docs = list(unique_docs.values())

    if not docs:
        print("No relevant articles found. Answering from general knowledge only.")
        prompt = f"""
Answer the following question using your own general knowledge. There are no articles provided.

Question:
{query}
"""
    else:
        print("\n📄 Relevant articles:\n")
        for i, doc in enumerate(docs, 1):
            print(f"{i}. {doc.metadata.get('title', 'No Title')}")
            print(f"   {doc.metadata.get('url', 'No URL')}\n")

        combined_content = "\n\n".join(doc.page_content for doc in docs)

        prompt = f"""
Answer the following question using your own general knowledge.
You may also incorporate relevant insights from recent news reports published by Lebanese and international media outlets, provided below.

Question:
{query}

Articles:
{combined_content}
"""

    response = llm.invoke(prompt)

    print("\n🧠 Final Answer:\n")
    print(response.content)


def summarize_article(url):
    print(f"\n🔎 Searching for article with URL: {url}")

    # Find the article in the vector DB
    docs = vector_store.similarity_search(url, k=5)

    found_doc = None
    for doc in docs:
        if doc.metadata.get('url') == url:
            found_doc = doc
            break

    if not found_doc:
        print("❌ Article not found in the database.")
        return

    print(f"Found article: {found_doc.metadata.get('title', 'No Title')}")

    prompt = f"""
Please summarize the following news article in a clear, neutral tone suitable for a general audience.

Title: {found_doc.metadata.get('title', 'No Title')}
Content:
{found_doc.page_content}
"""

    response = llm.invoke(prompt)

    print("\n📝 Summary:\n")
    print(response.content)
