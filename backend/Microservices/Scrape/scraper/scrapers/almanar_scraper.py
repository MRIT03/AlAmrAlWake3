from .base_scraper import BaseHomepageScraper
from bs4 import BeautifulSoup

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
