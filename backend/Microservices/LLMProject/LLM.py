import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from vector_query import query_articles  # <-- From your existing codebase

# --- Load API Key ---
load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

st.set_page_config(page_title="SamurAI", layout="centered")
st.title("📰 SamurAI — Lebanese News Assistant")

if not api_key:
    st.error("Gemini API key not found in environment variables.")
    st.stop()

genai.configure(api_key=api_key)

MODEL_NAME = 'gemini-2.5-flash-preview-04-17'
model = genai.GenerativeModel(MODEL_NAME)

# --- Session State Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "user",
        "content": (
            "You are SamurAI, created by Taline and Riad. "
            "You summarize and discuss Lebanese news based only on provided article sources."
            "Use formal but clear language."
        )
    })
    st.session_state.messages.append({
        "role": "model",
        "content": "Hello! How can I assist you with today's news?"
    })

# --- Display Chat History ---
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"] if message["role"] == "user" else "assistant"):
        st.markdown(message["content"])

# --- Chat Input ---
if prompt := st.chat_input("Ask about Lebanese news, events, or politicians..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Search ChromaDB for related articles ---
    related_articles = query_articles(prompt, k=5)  # Get up to 5 related articles

    context_message = ""
    if related_articles:
        context_message += "Based on articles from your database:\n\n"
        for article in related_articles:
            title = article.get('title', 'Untitled')
            source = article.get('source', 'Unknown Source')
            url = article.get('url', '#')
            context_message += f"- **{title}** ({source}) [Read here]({url})\n"
        context_message += "\nI will now answer your query considering these sources.\n"
    else:
        context_message = "No directly related articles were found in the database. I'll answer based on my knowledge."

    # --- Add the context to history ---
    st.session_state.messages.append({"role": "user", "content": context_message})

    # --- Prepare history for Gemini ---
    api_history_dicts = []
    for message in st.session_state.messages[:-1]:
        role = message["role"]
        if role in ["user", "model"]:
            api_history_dicts.append({
                "role": role,
                "parts": [{"text": message["content"]}]
            })

    # --- Call Gemini ---
    chat = model.start_chat(history=api_history_dicts)
    with st.spinner("Thinking..."):
        response = chat.send_message(prompt)

    reply = response.text if hasattr(response, 'text') else "(No response received.)"
    st.session_state.messages.append({"role": "model", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)

    # --- Offer to summarize any article ---
    if related_articles:
        st.markdown("**Would you like a summary of any of these articles?**")
        article_titles = [f"{a['title']} ({a['source']})" for a in related_articles]
        choice = st.selectbox("Pick an article:", ["No summary"] + article_titles)

        if choice != "No summary":
            selected_article = related_articles[article_titles.index(choice)]
            summary_prompt = (
                f"Please summarize this article:\n\n"
                f"Title: {selected_article['title']}\n\n"
                f"Content:\n{selected_article['content']}"
            )
            with st.spinner("Summarizing..."):
                summary_response = model.generate_content(summary_prompt)
            st.markdown("**Summary:**")
            st.markdown(summary_response.text if summary_response.text else "No summary available.")

st.markdown("---")
st.caption("Made with ❤ for the Software Engineering Project")
