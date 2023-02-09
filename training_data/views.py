from rest_framework.viewsets import ModelViewSet

from .models import Site, News
from .serializers import SiteSerializer, NewsSerializer


class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
