from abc import ABC, abstractmethod

class BaseScraper(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def scrape(self):
        """This method must be implemented by each scraper"""
        pass
