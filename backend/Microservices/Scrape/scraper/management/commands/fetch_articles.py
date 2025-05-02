#fetch_articles
from django.core.management.base import BaseCommand
from scraper.homepage_crawler import get_scraper_for_source
from scraper.models import Article, Log
from django.utils import timezone

class Command(BaseCommand):
    help = "Fetches articles from homepages, extracts content, saves to the database."

    def handle(self, *args, **kwargs):
        sources = ["mtv.com.lb", "lebanon24.com", "otv.com.lb"]

        for source in sources:
            scraper = get_scraper_for_source(source)
            if scraper is None:
                self.stderr.write(f"❌ No scraper found for {source}")
                continue

            self.stdout.write(f"🔎 Fetching homepage for {source}")
            try:
                homepage_html = scraper.fetch_homepage_html()
                article_links = scraper.extract_article_links(homepage_html)
            except Exception as e:
                self.stderr.write(f"❌ Error fetching homepage for {source}: {e}")
                continue

            self.stdout.write(f"Found {len(article_links)} articles on {source}")

            # Create a log for this scraping session
            log = Log.objects.create(
                scrapedSource=source,
                nbOfArticles=len(article_links),
                logDate=timezone.now()
            )

            for url in article_links:
                try:
                    if Article.objects.filter(url=url).exists():
                        self.stdout.write(f"🔁 Skipped duplicate: {url}")
                        continue

                    # extract_content now returns (title, content)
                    title, content = scraper.extract_content(url)

                    Article.objects.create(
                        log=log,
                        title=title or "No Title",
                        url=url,
                        content=content or "",
                        source=source  # Use the source domain, not the full URL
                    )
                    self.stdout.write(f"✅ Saved: {title or 'No Title'}")

                except Exception as e:
                    self.stderr.write(f"❌ Error saving {url}: {e}")

        self.stdout.write(self.style.SUCCESS("🎉 Finished fetching all articles."))