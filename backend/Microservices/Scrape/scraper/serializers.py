from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    # expose the FK as `log_id` rather than the full object
    log_id = serializers.PrimaryKeyRelatedField(source='log', read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',           # your PK
            'log_id',       # the Log FK
            'title',
            'url',
            'content',
            'source',
            'date_scraped',
        ]
