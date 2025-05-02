from .base_scraper import BaseHomepageScraper
from bs4 import BeautifulSoup

class MTVScraper(BaseHomepageScraper):
    BASE_URL = "https://www.mtv.com.lb"

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def extract_article_links(self, homepage_html):
        soup = BeautifulSoup(homepage_html, "html.parser")
        links = []
        for a_tag in soup.select('a[href^="/news/"]'):
            href = a_tag.get("href")
            if href and "news" in href and any(char.isdigit() for char in href):
                links.append(self.BASE_URL + href)
        return list(set(links))
