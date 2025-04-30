from .scrapers.almanar_scraper import AlManarScraper
# from .scrapers.mtv_scraper import MtvScraper
# Import more as needed...

class ScraperFactory:
    @staticmethod
    def get_scraper(site_name: str):
        scrapers = {
            'almanar': AlManarScraper,
            # 'mtv': MtvScraper,
            # Add other mappings here
        }

        scraper_class = scrapers.get(site_name.lower())
        if not scraper_class:
            raise ValueError(f"No scraper found for site: {site_name}")
        return scraper_class()
