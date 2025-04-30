import requests
from bs4 import BeautifulSoup
import re
from scraper.models import Article, Log
from datetime import datetime
import unicodedata
from .base_scraper import BaseScraper


class AlManarScraper(BaseScraper):
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.base_url = "https://english.almanar.com.lb"

    def get_recent_article_links(self, max_count):
        res = requests.get(self.base_url, headers=self.headers)
        soup = BeautifulSoup(res.text, "html.parser")

        links = []
        for a_tag in soup.select("div.post-title a[href]"):
            href = a_tag.get("href")
            if href and href.startswith(self.base_url):
                links.append(href)
            if len(links) >= max_count:
                break
        return links

    def clean_date_text(self, text):
        # Normalize weird spaces and strip
        text = unicodedata.normalize("NFKD", text).strip()
        return text.replace('\xa0', ' ').strip()

    def parse_article(self, url):
        res = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(res.text, "html.parser")

        title_tag = soup.find("h2")
        title = title_tag.get_text(strip=True) if title_tag else "No title"

        content_div = soup.find("div", class_="article-content")
        content = "\n\n".join(p.get_text(strip=True) for p in content_div.find_all("p")) if content_div else "No content"

        meta_spans = soup.select("div.article-meta span")
        pub_date = None
        for span in meta_spans:
            text = self.clean_date_text(span.get_text())
            try:
                pub_date = datetime.strptime(text, "%d %B %Y")
                break
            except ValueError:
                continue

        if not pub_date:
            print(f"[⚠️] Failed to parse date for: {url}")

        return {
            "title": title,
            "content": content,
            "date": pub_date,
            "url": url
        }

    def scrape(self, max_articles=10, start_date=None, end_date=None):
        urls = self.get_recent_article_links(50)
        articles_saved = 0

        for url in urls:
            if articles_saved >= max_articles:
                break

            data = self.parse_article(url)
            pub_date = data['date']

            if not pub_date:
                continue
            if start_date and pub_date < start_date:
                continue
            if end_date and pub_date > end_date:
                continue
            if Article.objects.filter(headline=data['title']).exists():
                continue

            log = Log.objects.create(
                logDate=datetime.now(),
                scrapedSource="Al-Manar",
                nbOfArticles=1
            )

            Article.objects.create(
                timeCreated=pub_date,
                headline=data['title'],
                thumbnail=None,
                body=data['content'],
                log=log
            )

            articles_saved += 1

        print(f"✅ {articles_saved} articles saved.")
