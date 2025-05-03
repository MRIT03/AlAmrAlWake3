from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET'])
def articles_up_to_date(request, date):
    """
    GET /api/articles/up-to/<YYYY-MM-DD>/
    Returns all Article objects whose date_scraped is on or before that date.
    """
    # 1) parse the incoming date string
    try:
        cutoff_day = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return Response(
            {'detail': 'Invalid date format. Use YYYY-MM-DD.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # 2) filter by the date portion of date_scraped
    qs = (
        Article.objects
        .filter(date_scraped__date__lte=cutoff_day)
        .order_by('-date_scraped')
    )

    # 3) serialize and return
    serializer = ArticleSerializer(qs, many=True)
    return Response(serializer.data)
