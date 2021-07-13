from rest_framework import fields, serializers
from api.models import ShortenedURL

class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['created', 'long_url', 'short_url', 'times_visited']