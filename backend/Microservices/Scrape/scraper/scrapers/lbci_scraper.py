from .base_scraper import BaseHomepageScraper
from bs4 import BeautifulSoup

class LBCIScraper(BaseHomepageScraper):
    BASE_URL = "https://www.lbcgroup.tv"

    def extract_article_links(self, homepage_html):
        soup = BeautifulSoup(homepage_html, "html.parser")
        links = []
        for a_tag in soup.select('a[href^="/news/"]'):
            href = a_tag.get("href")
            if href and any(char.isdigit() for char in href):
                full_url = self.BASE_URL + href
                links.append(full_url)
        return list(set(links))
