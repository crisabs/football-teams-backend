from rest_framework.routers import DefaultRouter
from match.api.views import MatchViewSet

app_name = "match"
router = DefaultRouter()
router.register(r"", MatchViewSet, basename="match")

urlpatterns = router.urls
