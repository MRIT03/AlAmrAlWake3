import requests
from bs4 import BeautifulSoup
from datetime import datetime

# --- Mapping dictionary to convert Arabic category names to English ---
category_map = {
    "سياسة": "Politics",
    "ناس": "People",
    "صحة": "Health",
    "مجتمع": "Society",
    "إقتصاد": "Economy",
    "فن": "Entertainment",   # or "Art/Entertainment"
    "منوعات": "Misc",
    "رياضة": "Sports",
    # Add more translations if needed
}

# --- Function to scrape the homepage and extract article links ---
def scrape_homepage(url, limit=10, category_filter="all", min_date=None):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the homepage!")
        return []
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Example: find all <a> tags and filter those that appear to be article links.
    # (You may need to adjust this selector based on the website.)
    article_links = soup.find_all('a', href=True)
    valid_links = []
    for link in article_links:
        href = link['href']
        # In this example we assume article links start with '/News/'
        if href.startswith("/News/"):
            valid_links.append(href)
    # Remove duplicates
    valid_links = list(set(valid_links))
    
    # Iterate over each article link, fetch and process its content.
    scraped_articles = []
    count = 0
    for relative_link in valid_links:
        # If we have reached the limit, break out of the loop.
        if count >= limit:
            break

        article_url = url.rstrip("/") + relative_link
        article_data = scrape_article(article_url)
        if article_data is None:
            continue

        # Convert the Arabic category to English (if the scraped category is known)
        article_cat_arabic = article_data.get('category', 'Unknown')
        article_cat_english = category_map.get(article_cat_arabic, article_cat_arabic)
        article_data['category'] = article_cat_english

        # Filter by date if min_date is specified.
        if min_date is not None and article_data.get('published_date'):
            if article_data['published_date'] < min_date:
                continue

        # Filter by category if the user did not select "all".
        if category_filter.lower() != "all":
            if article_cat_english.lower() != category_filter.lower():
                continue

        scraped_articles.append(article_data)
        count += 1
    
    return scraped_articles

# --- Function to scrape an individual article page ---
def scrape_article(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve article: {url}")
        return None
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Extract the title; in the sample HTML the title is in an <h1 id="article-title">
    title_tag = soup.find("h1", id="article-title")
    title = title_tag.get_text(strip=True) if title_tag else "No title found"
    
    # Extract the publication date. In the sample, it's in a <p id="publishedDate">
    published_date = None
    published_date_tag = soup.find("p", id="publishedDate")
    if published_date_tag:
        date_str = published_date_tag.get_text(strip=True)
        # The date is in Arabic. For example: "11 نيسان 2025 11:54"
        # Map Arabic month names to English:
        month_map = {
            "كانون الثاني": "January", "شباط": "February", "آذار": "March", "نيسان": "April",
            "أيار": "May", "حزيران": "June", "تموز": "July", "آب": "August", "أيلول": "September",
            "تشرين الأول": "October", "تشرين الثاني": "November", "كانون الأول": "December"
        }
        parts = date_str.split()
        if len(parts) >= 3:
            day = parts[0]
            month_ar = parts[1]
            year = parts[2]
            # Use the mapping to convert the Arabic month to English.
            month_en = month_map.get(month_ar, month_ar)
            # Reassemble the string; this example expects a format like "11 April 2025 11:54"
            new_date_str = " ".join([day, month_en, year] + parts[3:])
            try:
                published_date = datetime.strptime(new_date_str, "%d %B %Y %H:%M")
            except Exception as e:
                # In case of an error, print it and set published_date to None.
                print(f"Date parsing error for article {url}: {e}")
                published_date = None

    # Extract the category.
    # In our sample HTML the category (label) is in a <span class="label"> near the article image.
    label_tag = soup.find("span", class_="label")
    category = label_tag.get_text(strip=True) if label_tag else "Unknown"
    
    # Extract the main article text.
    article_body_tag = soup.find("div", id="article-MainText")
    content = article_body_tag.get_text(" ", strip=True) if article_body_tag else ""
    
    # Construct a dictionary with the scraped data.
    article_data = {
        "url": url,
        "title": title,
        "published_date": published_date,
        "category": category,
        "content": content
    }
    return article_data

# --- Main function to run the scraper ---
if __name__ == "__main__":
    # Example homepage URL for MTV Lebanon (ensure it ends with no trailing slash)
    homepage_url = "https://www.mtv.com.lb"
    
    # Define your options:
    # - limit: number of articles to scrape
    # - category_filter: in English; set to "all" if no filtering is desired.
    # - min_date: only scrape articles published on or after this date.
    #   For example, we set the minimum date to April 10, 2025.
    limit = 100
    category_filter = "all"  # Change this to, for example, "Economy" to filter articles by that category.
    min_date = datetime(2025, 4, 10, 0, 0)
    
    articles = scrape_homepage(homepage_url, limit=limit, category_filter=category_filter, min_date=min_date)
    if articles:
        for article in articles:
            print("URL:", article.get("url"))
            print("Title:", article.get("title"))
            print("Published Date:", article.get("published_date"))
            print("Category:", article.get("category"))
            print("Content (first 100 characters):", article.get("content")[:100])
            print("=" * 50)
    else:
        print("No articles were scraped with the applied filters.")
