from article_query import search_articles
from llm_answer_builder import build_answer

def main():
    print("🔎 Welcome to the News Assistant (LLM Powered)")
    query = input("What do you want to know about today?\n> ")

    # 1. Search your DB articles
    relevant_articles = search_articles(query, max_results=5)

    if not relevant_articles:
        print("No relevant articles found in your database.")
        return

    # 2. Build LLM answer
    answer, cited_articles = build_answer(query, relevant_articles)

    # 3. Output answer
    print("\n📝 Answer:\n")
    print(answer)

    # 4. Offer to summarize any articles
    if cited_articles:
        print("\nWould you like a summary of any of these articles?")
        for idx, article in enumerate(cited_articles, start=1):
            print(f"{idx}. {article['title']} - {article['url']}")

        choice = input("\nEnter the number of the article to summarize (or press Enter to skip): ")
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(cited_articles):
                selected = cited_articles[idx]
                print("\n🔎 Summary:\n")
                print(selected["content"][:1000] + "..." if selected["content"] else "No content available.")
            else:
                print("Invalid choice.")
        else:
            print("No article selected for summarization.")

if __name__ == "__main__":
    main()
