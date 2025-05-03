from .base_scraper import BaseHomepageScraper
from bs4 import BeautifulSoup
import requests

class LBCIScraper(BaseHomepageScraper):
    BASE_URL = "https://www.lbcgroup.tv"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    def extract_article_links(self, homepage_html):
        soup = BeautifulSoup(homepage_html, "html.parser")
        links = []
        for a_tag in soup.select('a[href^="/news/"]'):
            href = a_tag.get("href")
            if href and any(char.isdigit() for char in href):
                links.append(self.BASE_URL + href)
        return list(set(links))

    def extract_content(self, url):
        response = requests.get(url, headers=self.headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title else "No Title"
        content_div = soup.find("div", class_="article-body")
        content = content_div.get_text(separator=" ", strip=True) if content_div else ""
        return title, content
