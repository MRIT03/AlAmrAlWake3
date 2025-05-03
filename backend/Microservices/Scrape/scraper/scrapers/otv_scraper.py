from .base_scraper import BaseHomepageScraper
from bs4 import BeautifulSoup
import requests

class OTVScraper(BaseHomepageScraper):
    BASE_URL = "https://otv.com.lb"

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Connection": "keep-alive"
        }

    def extract_article_links(self, homepage_html):
        soup = BeautifulSoup(homepage_html, "html.parser")
        links = []
        for a_tag in soup.select('a[href^="https://otv.com.lb/lebanon-breaking-news/"]'):
            href = a_tag.get("href")
            if href:
                links.append(href)
        return list(set(links))

    def extract_content(self, url):
        response = requests.get(url, headers=self.headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title"

        paragraphs = soup.select("div.single_content p")
        content = "\n".join(p.get_text(strip=True) for p in paragraphs)

        return title, content
