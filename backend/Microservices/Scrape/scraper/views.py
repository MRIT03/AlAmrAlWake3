from django.shortcuts import render
from django.http import JsonResponse
from .models import Article
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.timezone import now

# Create your views here.
@csrf_exempt
def latest_articles(request):
    query = request.GET.get("q")
    source = request.GET.get("source")
    
    articles = Article.objects.all().order_by('-date_scraped')
    
    if query:
        articles = articles.filter(title__icontains=query)
    if source:
        articles = articles.filter(source__icontains=source)

    results = [
        {
            "title": a.title,
            "url": a.url,
            "source": a.source,
            "date_scraped": a.date_scraped.isoformat(),
            "content": a.content[:500] + "..."  # truncate preview
        }
        for a in articles[:10]
    ]
    
    return JsonResponse(results, safe=False, json_dumps_params={"ensure_ascii": False})

