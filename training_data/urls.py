from rest_framework.routers import SimpleRouter

from training_data.views import SiteViewSet, NewsViewSet


router = SimpleRouter(trailing_slash=False)
router.register('sites', SiteViewSet)
router.register('news', NewsViewSet)

urlpatterns = router.urls
