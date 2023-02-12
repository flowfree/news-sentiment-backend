from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from djangorestframework_camel_case.render import (
    CamelCaseJSONRenderer,
    CamelCaseBrowsableAPIRenderer,
)

from .models import Site, News
from .serializers import SiteSerializer, NewsSerializer


class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    renderer_classes = [CamelCaseJSONRenderer]

    def __init__(self, *args, **kwargs):
        if settings.DEBUG:
            self.renderer_classes += [CamelCaseBrowsableAPIRenderer]

        super().__init__(*args, **kwargs)
