from django.db import models


class Team(models.Model):
    name = models.CharField(unique=True, max_length=50)
    nickname = models.CharField(max_length=50)
    slogan = models.CharField(max_length=50)
    foundation_date = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    players = models.ManyToManyField(
        "player.Player", through="PlayerTeam", related_name="teams", blank=True
    )

    qty_followers = models.IntegerField(default=0, blank=True)
    founder = models.ForeignKey(
        "player.Player",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="founded_teams",
    )
    owner = models.ForeignKey(
        "player.Player",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_teams",
    )

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class PlayerTeamRole(models.TextChoices):
    FOLLOWER = "FOLLOWER", "Follower"
    PLAYER = "PLAYER", "Player"
    ADMIN = "ADMIN", "Admin"


class PlayerProposalStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    ACCEPTED = "ACCEPTED", "Accepted"
    REJECTED = "REJECTED", "Rejected"


class PlayerTeam(models.Model):
    player = models.ForeignKey(
        "player.Player", on_delete=models.CASCADE, related_name="memberships"
    )
    team = models.ForeignKey("Team", on_delete=models.CASCADE, related_name="members")
    membership_date = models.DateField(auto_now_add=True)
    matches_played = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    roles = models.ManyToManyField("Role", blank=True)

    class Meta:
        unique_together = ("player", "team")

    def __str__(self):
        return f"{self.player.nickname} in {self.team.name} as {', '.join(str(role) for role in self.roles.all())}"


class PlayerProposalTeam(models.Model):
    player = models.ForeignKey(
        "player.Player", on_delete=models.CASCADE, related_name="proposals"
    )
    team = models.ForeignKey("Team", on_delete=models.CASCADE, related_name="proposals")
    role = models.CharField(
        max_length=20, choices=PlayerTeamRole.choices, default=PlayerTeamRole.PLAYER
    )
    proposal_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=PlayerProposalStatus.choices,
        default=PlayerProposalStatus.PENDING,
    )
    response_date = models.DateField(null=True, blank=True)
    proposal_message = models.TextField(blank=True)
    response_message = models.TextField(blank=True)

    class Meta:
        unique_together = ("player", "team")
