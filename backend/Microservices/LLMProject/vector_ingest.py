import sqlite3
import chromadb
from article_vectorizer import vectorize_text

# Connect to your SQLite DB
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

cursor.execute("SELECT id, title, content, url, source_name FROM scraper_article")
rows = cursor.fetchall()

conn.close()

# Initialize Chroma collection
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="articles")

# Prepare data
ids = []
texts = []
metadatas = []

for row in rows:
    article_id, title, content, url, source_name = row
    text = f"{title}. {content or ''}"
    ids.append(str(article_id))
    texts.append(text)
    metadatas.append({
        "title": title,
        "url": url,
        "source_name": source_name
    })

# Vectorize and add to Chroma
from tqdm import tqdm

for idx, text in tqdm(zip(ids, texts), total=len(ids), desc="Indexing articles"):
    vector = vectorize_text(text)
    collection.add(
        ids=[idx],
        embeddings=[vector.tolist()],
        documents=[text],
        metadatas=[metadatas[int(idx)-1]]
    )

print("✅ Finished indexing all articles into Chroma.")
