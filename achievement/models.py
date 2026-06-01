from django.db import models
from player.models import Player
from team.models import Team


class Achievement(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True, db_index=True)
    description = models.TextField(blank=True)


class PlayerAchievement(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="player_achievements"
    )
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        related_name="player_achievements",
    )
    acquired_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("player", "achievement")


class TeamAchievement(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team_achievements"
    )
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        related_name="team_achievements",
    )
    acquired_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("team", "achievement")
