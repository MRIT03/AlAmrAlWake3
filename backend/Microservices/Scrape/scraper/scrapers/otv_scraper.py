from .base_scraper import BaseHomepageScraper
from bs4 import BeautifulSoup

class OTVScraper(BaseHomepageScraper):
    BASE_URL = "https://otv.com.lb"

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def extract_article_links(self, homepage_html):
        soup = BeautifulSoup(homepage_html, "html.parser")
        links = []
        for a_tag in soup.select('a[href^="https://otv.com.lb/lebanon-breaking-news/"]'):
            href = a_tag.get("href")
            if href:
                links.append(href)
        return list(set(links))
