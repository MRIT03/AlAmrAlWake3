from .base_scraper import BaseHomepageScraper
from bs4 import BeautifulSoup
import requests

class AlJadeedScraper(BaseHomepageScraper):
    BASE_URL = "https://www.aljadeed.tv"

    def __init__(self):
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/123.0.0.0 Safari/537.36"
            )
        }

    def extract_article_links(self, homepage_html):
        soup = BeautifulSoup(homepage_html, "html.parser")
        links = []
        for a_tag in soup.select('a[href^="https://www.aljadeed.tv/"]'):
            href = a_tag.get("href")
            if href and "/arabic/news/" in href:
                links.append(href)
        return list(set(links))

    def extract_content(self, url):
        response = requests.get(url, headers=self.headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Title from the <title> tag
        title = soup.title.string.strip() if soup.title else "No Title"

        # --- Main content ---
        # Al Jadeed puts the main article text inside this specific span:
        content_span = soup.find(
            "span", id="ctl00_MainContent_ArticleDetailsDescription21_lblShortDesc"
        )

        if content_span:
            content = content_span.get_text(strip=True)
        else:
            # Fallback: get all <p> tags in case the span is missing
            paragraphs = soup.find_all("p")
            content = "\n".join(
                p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)
            )

        return title, content
