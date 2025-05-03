# app.py

import streamlit as st
import google.generativeai as genai
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
from index_articles import get_articles_from_db  # We'll use this to reindex if needed

load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

# --- Gemini setup ---
genai.configure(api_key=api_key)
MODEL_NAME = 'gemini-2.5-flash-preview-04-17'
model = genai.GenerativeModel(MODEL_NAME)

# --- Chroma setup ---
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key
)

vector_store = Chroma(
    collection_name="embeddings",
    embedding_function=embeddings,
    persist_directory="./vector_db"
)

# --- Streamlit UI ---
st.title("📰 Lebanese News AI Assistant")

question = st.text_input("Ask me anything about recent news:")

if question:
    similar_docs = vector_store.similarity_search(question, k=4)

    context = ""
    for doc in similar_docs:
        context += f"Title: {doc.metadata['title']}\nSource: {doc.metadata['source']}\nContent: {doc.page_content}\n\n"

    full_prompt = f"""
You are an AI that answers questions using both your general knowledge and the provided articles from Lebanese news outlets.
If relevant, mention what the news outlets say and cite the article title and source. Answer the user's question:
'{question}'

Here are the articles:
{context}
"""

    response = model.generate_content(full_prompt)
    st.subheader("Answer:")
    st.write(response.text)

    if similar_docs:
        st.markdown("---")
        st.subheader("Would you like to summarize one of the articles I used?")
        options = [f"{doc.metadata['title']} ({doc.metadata['source']})" for doc in similar_docs]
        choice = st.selectbox("Select article to summarize:", ["None"] + options)

        if choice != "None":
            idx = options.index(choice)
            article = similar_docs[idx]
            summary_prompt = f"Summarize this article:\n\n{article.page_content}"
            summary = model.generate_content(summary_prompt)
            st.subheader("Summary:")
            st.success(summary.text)
