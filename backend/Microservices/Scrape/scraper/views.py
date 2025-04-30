from django.shortcuts import render
from django.http import JsonResponse
from .scraper_factory import ScraperFactory

def scrape_news(request, site_name):
    try:
        scraper = ScraperFactory.get_scraper(site_name)
        scraper.scrape()
        return JsonResponse({'status': 'success', 'site': site_name})
    except ValueError as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

# Create your views here.
