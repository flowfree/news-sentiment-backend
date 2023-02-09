"""news_sentiment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.routers import SimpleRouter

from training_data.views import SiteViewSet, NewsViewSet


class HomeView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'quote': settings.SAMPLE_QUOTE,
            'time': timezone.now().isoformat()
        })


router = SimpleRouter(trailing_slash=False)
router.register('sites', SiteViewSet)
router.register('news', NewsViewSet)


urlpatterns = [
    path('', HomeView.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
