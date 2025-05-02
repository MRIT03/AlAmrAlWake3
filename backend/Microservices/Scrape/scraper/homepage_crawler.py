# homepage_crawler.py
from scraper.scrapers.mtv_scraper import MTVScraper
from scraper.scrapers.lebanon24_scraper import Lebanon24Scraper
from scraper.scrapers.otv_scraper import OTVScraper
from scraper.scrapers.lbci_scraper import LBCIScraper
from scraper.scrapers.aljadeed_scraper import AlJadeedScraper
from scraper.scrapers.almanar_scraper import AlManarScraper

SCRAPER_MAP = {
    "mtv.com.lb": MTVScraper(),
    "lebanon24.com": Lebanon24Scraper(),
    "otv.com.lb": OTVScraper(),
    "lbcgroup.tv": LBCIScraper(),
    "aljadeed.tv": AlJadeedScraper(),
    "almanar.com.lb": AlManarScraper(),
}

def get_scraper_for_source(source):
    return SCRAPER_MAP.get(source)
