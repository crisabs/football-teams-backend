from django.urls import path
from team.api.views import TeamCreateAPIView

app_name = "team"

urlpatterns = [
    path("team-create/", TeamCreateAPIView.as_view(), name="team_create"),
]
