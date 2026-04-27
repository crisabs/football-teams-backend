from django.db import models
from player.models import Player


class Team(models.Model):
    name = models.CharField(unique=True, max_length=50)
    nickname = models.CharField(max_length=50)
    slogan = models.CharField(max_length=50)

    foundation_date = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    players = models.ManyToManyField(Player, related_name="teams", blank=True)
    founder = models.CharField(max_length=50)

    followers = models.ManyToManyField(
        Player, related_name="followed_teams", blank=True
    )

    founder = models.ForeignKey(
        Player,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="founded_teams",
    )
    owner = models.ForeignKey(
        Player,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_teams",
    )

    def __str__(self):
        return self.name
