from django.core.management.base import BaseCommand
from scraper.tavily_client import query_tavily
from scraper.models import Article, Log
from django.utils import timezone

# List of known homepage/section URL patterns to skip
HOMEPAGE_PREFIXES = [
    "https://www.mtv.com.lb/en/",
    "https://www.mtv.com.lb/",
    "https://www.lebanon24.com/",
    "https://otv.com.lb/",
    "https://www.lbcgroup.tv/",
    "https://english.almanar.com.lb/",
    "https://almanar.com.lb/",
    "https://www.elnashra.com/",
    "https://www.annahar.com/",
    "https://www.nna-leb.gov.lb/",
    "https://www.aljazeera.com/where/lebanon"
]

class Command(BaseCommand):
    help = "Fetches articles from Tavily and stores them in the database."

    def handle(self, *args, **kwargs):
        queries = [
            "site:mtv.com.lb Lebanon",
            "site:lebanon24.com Lebanon",
            "site:otv.com.lb Lebanon",
            "site:lbcgroup.tv Lebanon",
            "site:almanar.com.lb Lebanon",
            "site:elnashra.com Lebanon",
            "site:annahar.com Lebanon",
            "site:nna-leb.gov.lb Lebanon",
            "site:aljazeera.com Lebanon"
        ]

        for query in queries:
            self.stdout.write(f"🔍 Fetching: {query}")
            try:
                results = query_tavily(query, max_results=5)
            except Exception as e:
                self.stderr.write(f"Error fetching from Tavily: {e}")
                continue

            log = Log.objects.create(
                scrapedSource=query,
                nbOfArticles=len(results),
                logDate=timezone.now()
            )

            for article_data in results:
                url = article_data["url"]
                # Skip if the URL matches a known homepage or category URL
                if any(url.startswith(prefix) for prefix in HOMEPAGE_PREFIXES):
                    self.stdout.write(f"Skipped (homepage or category): {url}")
                    continue

                try:
                    Article.objects.create(
                        log=log,
                        title=article_data["title"],
                        url=url,
                        content=article_data.get("content", ""),
                        source=url.split('/')[2]
                    )
                    self.stdout.write(f"Saved: {article_data['title']}")
                except Exception as e:
                    self.stderr.write(f"Skipped duplicate or error: {e}")

        self.stdout.write(self.style.SUCCESS("Finished fetching articles."))

        # Automatically push to vector DB
        import subprocess
        subprocess.run(["python", "push_to_vector_db.py"])
        self.stdout.write(self.style.SUCCESS("Vector DB updated with new articles."))