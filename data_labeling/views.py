from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from djangorestframework_camel_case.render import (
    CamelCaseJSONRenderer,
    CamelCaseBrowsableAPIRenderer,
)

from .models import Site, News
from .serializers import SiteSerializer, NewsSerializer
from .exceptions import ScraperError


if settings.DEBUG:
    renderers = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
else:
    renderers = [CamelCaseJSONRenderer]


class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    renderer_classes = renderers


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    renderer_classes = renderers

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ScraperError as e:
            return Response({'error': [f'{e}']}, status=500)
