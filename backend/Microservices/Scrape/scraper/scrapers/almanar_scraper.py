from .base_scraper import BaseHomepageScraper
from bs4 import BeautifulSoup
import requests

class AlManarScraper(BaseHomepageScraper):
    BASE_URL = "https://www.almanar.com.lb"

    def extract_article_links(self, homepage_html):
        soup = BeautifulSoup(homepage_html, "html.parser")
        links = []
        for a_tag in soup.select('a[href^="https://www.almanar.com.lb/"]'):
            href = a_tag.get("href")
            if href and any(char.isdigit() for char in href):
                links.append(href)
        return list(set(links))

    def extract_content(self, url):
        response = requests.get(url, headers=self.headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title"

        # Grab the article content properly
        body = soup.select_one("div.article-content")
        content = body.get_text(separator="\n").strip() if body else ""

        return title, content
