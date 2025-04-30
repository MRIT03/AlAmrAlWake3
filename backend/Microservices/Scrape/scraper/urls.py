from django.urls import path
from .views import scrape_news

urlpatterns = [
    path('scrape/<str:site_name>/', scrape_news), #CHANGE HEREEEEEE
]
