from django.db import models
from player.models import Player
from team.models import Team


class Achievement(models.Model):
    name = models.CharField()
    code = models.CharField(max_length=50, unique=True, db_index=True)
    description = models.CharField(default="", max_length=50)


class PlayerAchievement(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="player_achievement"
    )
    achievements = models.ManyToManyField(
        "Achievement", blank=True, related_name="player_owners"
    )
    description = models.CharField(default="", max_length=50)
    acquired_at = models.DateTimeField(auto_now_add=True)


class TeamAchievement(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team_achievement"
    )
    achievements = models.ManyToManyField(
        "Achievement", blank=True, related_name="team_owners"
    )
    description = models.CharField(default="", max_length=50)
    acquired_at = models.DateTimeField(auto_now_add=True)
