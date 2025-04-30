from django.core.management.base import BaseCommand
from scraper.tavily_client import query_tavily
from scraper.models import Article, Log
from django.utils import timezone

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
                try:
                    Article.objects.create(
                        log=log,
                        title=article_data["title"],
                        url=article_data["url"],
                        content=article_data.get("content", ""),
                        source=article_data["url"].split('/')[2]
                    )
                    self.stdout.write(f"Saved: {article_data['title']}")
                except Exception as e:
                    self.stderr.write(f"Skipped duplicate or error: {e}")

        self.stdout.write(self.style.SUCCESS("Finished fetching articles."))
