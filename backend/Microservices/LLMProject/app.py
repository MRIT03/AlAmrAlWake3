import streamlit as st
import os
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
import google.generativeai as genai
from tavily import TavilyClient

# ---------- CONFIG ----------
load_dotenv()

api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    st.error("GOOGLE_GEMINI_API_KEY missing.")
    st.stop()

if not tavily_key:
    st.warning("Tavily API key missing. Web search fallback won't work.")
else:
    tavily_client = TavilyClient(api_key=tavily_key)

genai.configure(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash-preview-04-17"

# ---------- VECTOR DB ----------
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key
)

vector_store = Chroma(
    collection_name="news_articles",
    embedding_function=embeddings,
    persist_directory="./vector_db"
)

retriever = vector_store.as_retriever(search_kwargs={"k": 4})

# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="🥷 SamurAI — Lebanon News Chatbot", layout="centered")
st.title("🥷 SamurAI — Lebanon News Chatbot")
st.caption("Your Lebanese news assistant powered by Gemini.")

# ---------- SESSION STATE ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "references" not in st.session_state:
    st.session_state.references = []

# ---------- HELPER FUNCTIONS ----------

def format_references(docs, start_idx=1):
    refs = []
    for idx, doc in enumerate(docs, start=start_idx):
        meta = doc.metadata
        refs.append({
            "id": idx,
            "title": meta.get("title", "No Title"),
            "url": meta.get("url", "#"),
            "source": meta.get("source", "Unknown"),
            "date": meta.get("date", "Unknown"),
            "content": doc.page_content
        })
    return refs

def build_context(docs):
    context = ""
    for idx, doc in enumerate(docs, start=1):
        meta = doc.metadata
        context += f"[{idx}] {meta.get('source', 'Unknown')} - \"{meta.get('title', 'No Title')}\" ({meta.get('date', 'Unknown')}): {doc.page_content}\n\n"
    return context

def build_markdown_citations(refs):
    if not refs:
        return "_No articles found._"
    citations = []
    for ref in refs:
        link = f"[{ref['title']}]({ref['url']})"
        citations.append(f"[{ref['id']}] {ref['source']} - {link} ({ref['date']})")
    return "\n".join(citations)

def match_reference(user_input):
    for ref in st.session_state.references:
        if str(ref["id"]) in user_input:
            return ref
        if ref["title"].lower() in user_input.lower():
            return ref
    return None

def summarize_article(content):
    model = genai.GenerativeModel(MODEL_NAME)
    prompt = f"Summarize the following article:\n\n{content}"
    response = model.generate_content(prompt)
    return response.text.strip() if response.text else "No summary available."

def search_tavily(query):
    results = []
    try:
        tavily_results = tavily_client.search(
            query=query,
            search_depth="advanced",
            max_results=5
        )["results"]

        for idx, r in enumerate(tavily_results):
            doc = Document(
                page_content=r["content"] or r["title"],
                metadata={
                    "title": r["title"],
                    "url": r["url"],
                    "source": "Web (Tavily)",
                    "date": "Latest"
                }
            )
            results.append(doc)
    except Exception as e:
        st.warning(f"Tavily search failed: {e}")

    return results

# ---------- CHAT HISTORY ----------
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(chat["user"])
    with st.chat_message("assistant"):
        st.markdown(chat["assistant"])

# ---------- CHAT INPUT ----------
query = st.chat_input("Ask a question or request an article summary...")

if not query and not st.session_state.chat_history:
    with st.chat_message("assistant"):
        st.markdown("Hello! 👋 How can I help you today? You can ask questions or request article summaries.")

if query:
    with st.chat_message("user"):
        st.markdown(query)

    # ---------- SUMMARIZATION HANDLER ----------
    ref = match_reference(query)
    if any(kw in query.lower() for kw in ["summarize", "summary", "summarise"]) and ref:
        with st.chat_message("assistant"):
            st.markdown(f"**Summary for:** {ref['title']}")
            with st.spinner("🥷 SamurAI is summarizing..."):
                summary = summarize_article(ref["content"])
            st.success(summary)
            st.session_state.chat_history.append({"user": query, "assistant": summary})

    else:
        # ---------- CONTEXT RETRIEVAL ----------
        relevant_docs = retriever.get_relevant_documents(query)
        st.session_state.references = format_references(relevant_docs)

        if len(relevant_docs) < 2 and tavily_key:
            web_docs = search_tavily(query)
            all_docs = relevant_docs + web_docs
            st.session_state.references = format_references(all_docs)
        else:
            all_docs = relevant_docs

        context = build_context(all_docs)

        # ---------- GEMINI PROMPT ----------
        system_prompt = (
            f"You are SamurAI, a Lebanese news expert assistant. Use the context below to answer the user's question. "
            f"Include citations in the form [n] linking to the article's source. If no relevant context exists, answer using general knowledge."
            f"\n\nContext:\n{context}\n\nUser Question: {query}"
        )

        model = genai.GenerativeModel(MODEL_NAME)

        with st.chat_message("assistant"):
            with st.spinner("🥷 SamurAI is thinking..."):
                response = model.generate_content(system_prompt)
            reply = response.text.strip() if response.text else "I couldn't generate a response."

            st.markdown(reply)

            # ---------- REFERENCES ----------
            st.markdown("### References")
            st.markdown(build_markdown_citations(st.session_state.references), unsafe_allow_html=True)

            st.info("Tip: You can say things like 'Summarize article 1' or 'Summarize \"Title\"' anytime.")

        # ---------- SAVE TO CHAT HISTORY ----------
        st.session_state.chat_history.append({"user": query, "assistant": reply})

st.markdown("---")
st.markdown("Made with ❤ for the Software Engineering Class")