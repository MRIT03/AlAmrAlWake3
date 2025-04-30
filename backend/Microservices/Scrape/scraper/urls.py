from django.urls import path
from .views import latest_articles

urlpatterns = [
    path("api/articles/", latest_articles, name="latest_articles"),
]
