from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup

class BaseHomepageScraper(ABC):
    BASE_URL = ""

    def fetch_homepage_html(self):
        response = requests.get(self.BASE_URL, timeout=10)
        response.raise_for_status()
        return response.text

    @abstractmethod
    def extract_article_links(self, homepage_html):
        pass

    # ✅ NEW: default extract_content for all scrapers
    def extract_content(self, url):
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title else "No Title"
        content = ""  # You can improve this later
        return title, content
