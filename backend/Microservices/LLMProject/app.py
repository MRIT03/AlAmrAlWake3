import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from vector_search import search_articles

# --- API Key Configuration ---
load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

st.set_page_config(page_title="SamurAI", layout="centered")
st.title("💬 SamurAI")

if not api_key:
    st.error("Gemini API key not found in environment variables.")
    st.stop()

# --- Configure Gemini ---
try:
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"Failed to configure Gemini API: {e}")
    st.stop()

# --- Model Initialization ---
MODEL_NAME = 'gemini-2.5-flash-preview-04-17'

try:
    model = genai.GenerativeModel(MODEL_NAME)
except Exception as e:
    st.error(f"Failed to initialize Gemini model '{MODEL_NAME}': {e}")
    st.stop()

# --- Session State for Chat History ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "user",
        "content": ("You are SamurAI, created by Taline and Riad. "
                    "You help summarize news articles from local Lebanese media outlets. "
                    "You only follow the tone and style of each article. "
                    "Act as impressive as you can. Refer to Lebanese politics when needed.")
    })
    st.session_state.messages.append({
        "role": "model",
        "content": "Hello! How can I help you today?"
    })

# --- Display Chat History ---
for message in st.session_state.messages[1:]:  # Skip system prompt
    with st.chat_message(message["role"] if message["role"] == "user" else "assistant"):
        st.markdown(message["content"])

# --- Chat Input ---
if prompt := st.chat_input("What's on your mind?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Search vector DB for relevant articles ---
    docs = search_articles(prompt, k=3)

    if docs:
        combined_content = "\n\n".join(d.page_content for d in docs)
        debug_articles = "\n".join(
            [f"- [{doc.metadata['title']}]({doc.metadata['url']})" for doc in docs]
        )
        prompt_with_context = (f"Based on the following articles, answer the question:\n\n"
                               f"{prompt}\n\nArticles:\n{combined_content}")
    else:
        combined_content = None
        debug_articles = "No relevant articles found."
        prompt_with_context = prompt  # Ask Gemini without extra context

    # --- Prepare chat history for Gemini ---
    api_history_dicts = []
    for message in st.session_state.messages[:-1]:
        role = message["role"]
        if role not in ["user", "model"]:
            continue
        api_history_dicts.append({
            "role": role,
            "parts": [{"text": message["content"]}]
        })

    try:
        chat = model.start_chat(history=api_history_dicts)
        with st.spinner("I'm thinking, give me a second..."):
            response = chat.send_message(prompt_with_context)

        model_response_content = response.text.strip() if response.text else "(No response from Gemini.)"

        st.session_state.messages.append({"role": "model", "content": model_response_content})

        with st.chat_message("assistant"):
            st.markdown(model_response_content)

        # --- Optional: Show which articles were used ---
        if combined_content:
            with st.expander("🔎 Articles used for this answer"):
                st.markdown(debug_articles)

    except Exception as e:
        st.error(f"An error occurred while calling Gemini: {e}")
