from rest_framework.routers import SimpleRouter

from data_labeling.views import SiteViewSet, NewsViewSet


router = SimpleRouter(trailing_slash=False)
router.register('sites', SiteViewSet, basename='site')
router.register('news', NewsViewSet, basename='news')

urlpatterns = router.urls
