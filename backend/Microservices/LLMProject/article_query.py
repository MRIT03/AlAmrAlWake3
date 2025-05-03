import sqlite3

def search_articles(query, max_results=5):
    """
    Search your SQLite DB for relevant articles.
    """
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    sql = """
    SELECT title, content, url, source_name
    FROM scraper_article
    WHERE content LIKE ? OR title LIKE ?
    ORDER BY id DESC
    LIMIT ?
    """
    wildcard_query = f"%{query}%"
    cursor.execute(sql, (wildcard_query, wildcard_query, max_results))
    results = cursor.fetchall()

    articles = []
    for title, content, url, source_name in results:
        articles.append({
            "title": title,
            "content": content or "",
            "url": url,
            "source_name": source_name
        })

    conn.close()
    return articles
