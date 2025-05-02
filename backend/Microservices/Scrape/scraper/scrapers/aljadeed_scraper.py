from .base_scraper import BaseHomepageScraper
from bs4 import BeautifulSoup
import requests

class AlJadeedScraper(BaseHomepageScraper):
    BASE_URL = "https://www.aljadeed.tv"

    def extract_article_links(self, homepage_html):
        soup = BeautifulSoup(homepage_html, "html.parser")
        links = []
        for a_tag in soup.select('a[href^="/news/"]'):
            href = a_tag.get("href")
            if href and any(char.isdigit() for char in href):
                full_url = self.BASE_URL + href
                links.append(full_url)
        return list(set(links))

    def extract_content(self, url):
        response = requests.get(url, headers=self.headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title"

        content_div = soup.select_one("div.LongDesc.text-title-9")
        content = content_div.get_text(separator="\n", strip=True) if content_div else ""

        return title, content
