from django.db import models
from player.models import Player


class Achievement(models.Model):
    name = models.CharField()
    code = models.CharField(max_length=50, unique=True, db_index=True)
    description = models.CharField(default="", max_length=50)


class PlayerAchievement(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="player_achievement"
    )
    achievement = models.ForeignKey(
        Achievement, on_delete=models.CASCADE, related_name="owners"
    )
    description = models.CharField(default="", max_length=50)
    acquired_at = models.DateTimeField(auto_now_add=True)
