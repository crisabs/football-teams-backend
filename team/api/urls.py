from django.urls import path
from team.api.views import (
    TeamCreateAPIView,
    TeamDetailAPIView,
    TeamJoinRequestAPIView,
    TeamJoinRequestListAPIView,
)

app_name = "team"

urlpatterns = [
    path("team-create/", TeamCreateAPIView.as_view(), name="team_create"),
    path(
        "team-details/",
        TeamDetailAPIView.as_view(),
        name="team_details",
    ),
    path(
        "team-join-request/", TeamJoinRequestAPIView.as_view(), name="team_join_request"
    ),
    path(
        "team-join-request-list/",
        TeamJoinRequestListAPIView.as_view(),
        name="team_join_request_list",
    ),
]
