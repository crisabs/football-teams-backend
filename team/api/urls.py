from django.urls import path
from team.api.views import TeamCreateAPIView, TeamDetailAPIView

app_name = "team"

urlpatterns = [
    path("team-create/", TeamCreateAPIView.as_view(), name="team_create"),
    path(
        "team-details/",
        TeamDetailAPIView.as_view(),
        name="team_details",
    ),
]
