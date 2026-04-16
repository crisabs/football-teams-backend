from django.urls import path
from player.api.views import PlayerMeDetailsAPIView, PlayerNickAPIView

app_name = "player"

urlpatterns = [
    path("me/", PlayerMeDetailsAPIView.as_view(), name="player_me"),
    path("nick/", PlayerNickAPIView.as_view(), name="nick"),
]
