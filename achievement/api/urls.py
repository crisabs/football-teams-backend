from django.urls import path
from achievement.api.views import AchievementAcquiredView

app_name = "inventory"

urlpatterns = [
    path(
        "achievement-acquired/",
        AchievementAcquiredView.as_view(),
        name="achievement_acquired",
    ),
]
