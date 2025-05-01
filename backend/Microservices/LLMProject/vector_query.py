from vector_search import search_articles
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-preview-04-17",
    google_api_key=api_key
)

def ask_articles(query):
    print(f"\n🔍 You asked: {query}")
    docs = search_articles(query)

    print("\n📄 Relevant articles:\n")
    for i, doc in enumerate(docs, 1):
        print(f"{i}. {doc.metadata['title']}")
        print(f"   {doc.metadata['url']}\n")

    combined_content = "\n\n".join(d.page_content for d in docs)
    prompt = f"Based on the following articles, answer the question:\n\n{query}\n\nArticles:\n{combined_content}"

    response = llm.invoke(prompt)

    print("\nSummary:\n")
    print(response.content)
