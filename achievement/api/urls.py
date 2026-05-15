from django.urls import path
from achievement.api.views import (
    PlayerAchievementAcquireView,
    TeamAchievementAcquireView,
    PlayerAchievementListView,
    TeamAchievementListView,
)

app_name = "inventory"

urlpatterns = [
    path(
        "player-achievement-acquired/",
        PlayerAchievementAcquireView.as_view(),
        name="player_achievement_acquired",
    ),
    path(
        "team-achievement-acquired/",
        TeamAchievementAcquireView.as_view(),
        name="team_achievement_acquired",
    ),
    path(
        "player-achievement-list/",
        PlayerAchievementListView.as_view(),
        name="player_achievement_list",
    ),
    path(
        "team-achievement-list/",
        TeamAchievementListView.as_view(),
        name="team_achievement_list",
    ),
]
