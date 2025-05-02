from .base_scraper import BaseHomepageScraper
from bs4 import BeautifulSoup
import requests
class Lebanon24Scraper(BaseHomepageScraper):
    BASE_URL = "https://www.lebanon24.com"

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def extract_article_links(self, homepage_html):
        soup = BeautifulSoup(homepage_html, "html.parser")
        links = []
        for a_tag in soup.select('a[href^="/news/lebanon/"]'):
            href = a_tag.get("href")
            if href and any(char.isdigit() for char in href):
                links.append(self.BASE_URL + href)
        return list(set(links))

    def extract_content(self, url):
        response = requests.get(url, headers=self.headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title"

        # Target the article body
        article_body = soup.select_one("div.Article_Details_Desc.article_body_text")
        if not article_body:
            return title, ""

        # Collect all visible text inside, joining multiple small <div>s and <br>s
        content = article_body.get_text(separator="\n", strip=True)

        return title, content
