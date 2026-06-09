from django.db import models
from team.models import Team

class PlayerMatch(models.Model):
    player = models.ForeignKey(
        "player.Player", on_delete=models.CASCADE, related_name="matches"
    )
    match = models.ForeignKey("Match", on_delete=models.CASCADE, related_name="players")
    score = models.IntegerField(default=0)
    performance_notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("player", "match")

    def __str__(self):
        return f"{self.player.nickname} - {self.match.name}"


class Match(models.Model):
    name = models.CharField(max_length=100, blank=True)
    match_id = models.CharField(max_length=50, unique=True)
    league = models.CharField(max_length=100)
    spectators = models.IntegerField(default=0, blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    visiting_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="visiting_matches"
    )
    home_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="home_matches"
    )
    score_home = models.IntegerField(default=0)
    score_visiting = models.IntegerField(default=0)

    def __str__(self):
        return self.name
