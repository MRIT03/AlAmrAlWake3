from .base_scraper import BaseHomepageScraper
from bs4 import BeautifulSoup
import requests

class AlManarScraper(BaseHomepageScraper):
    BASE_URL = "https://www.almanar.com.lb"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    def extract_article_links(self, homepage_html):
        soup = BeautifulSoup(homepage_html, "html.parser")
        links = []
        for a_tag in soup.select('a[href^="https://www.almanar.com.lb/"]'):
            href = a_tag.get("href")
            if href and href.strip().endswith(tuple("0123456789")):  # Only actual articles, skip categories/tags
                links.append(href)
        return list(set(links))

    def extract_content(self, url):
        response = requests.get(url, headers=self.headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title else "No Title"
        content_div = soup.find("div", class_="entry-content")
        content = content_div.get_text(separator=" ", strip=True) if content_div else ""
        return title, content
