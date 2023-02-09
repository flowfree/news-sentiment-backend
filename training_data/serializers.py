from rest_framework.serializers import ModelSerializer
from .models import Site, News


class SiteSerializer(ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name', 'url', 'created_at', 'updated_at']


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'url', 'title', 'description', 'sentiment',
                  'created_at', 'updated_at']
