from rest_framework.serializers import ModelSerializer
from .models import Site, News


class SiteSerializer(ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name', 'url', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not in the `fields` argument
            allowed = set(fields)
            existing = set(self.fields)
            for f in existing - allowed:
                self.fields.pop(f)


class NewsSerializer(ModelSerializer):
    site = SiteSerializer(read_only=True, fields=['id', 'name'])

    class Meta:
        model = News
        fields = ['id', 'url', 'site', 'title', 'description', 
                  'image_url', 'sentiment', 'published_time', 
                  'created_at', 'updated_at']
