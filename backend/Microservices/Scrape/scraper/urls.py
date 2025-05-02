from django.urls import path
from .views import articles_up_to_date

urlpatterns = [
    path(
        'articles/up-to/<str:date>/',
        articles_up_to_date,
        name='articles-up-to-date'
    ),
]
