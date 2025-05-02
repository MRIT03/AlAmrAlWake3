#homepage_crawler.py
from scraper.scrapers.mtv_scraper import MTVScraper
from scraper.scrapers.lebanon24_scraper import Lebanon24Scraper
from scraper.scrapers.otv_scraper import OTVScraper

SCRAPER_MAP = {
    "mtv.com.lb": MTVScraper(),
    "lebanon24.com": Lebanon24Scraper(),
    "otv.com.lb": OTVScraper(),
}

def get_scraper_for_source(source):
    return SCRAPER_MAP.get(source)
