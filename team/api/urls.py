from django.urls import path
from team.api.views import (
    TeamCreateAPIView,
    TeamDetailAPIView,
    TeamJoinRequestAPIView,
    TeamJoinRequestListAPIView,
    TeamLeaveAPIView,
    TeamAcceptPlayerJoinRequestAPIView,
    TeamDeleteAPIView,
    TeamFollowAPIView,
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
    path("team-leave/", TeamLeaveAPIView.as_view(), name="team_leave"),
    path(
        "team-accept-join-request/",
        TeamAcceptPlayerJoinRequestAPIView.as_view(),
        name="team_accept_join_request",
    ),
    path(
        "team-delete/",
        TeamDeleteAPIView.as_view(),
        name="team_delete",
    ),
    path(
        "team-follow/",
        TeamFollowAPIView.as_view(),
        name="team_follow",
    ),
]
