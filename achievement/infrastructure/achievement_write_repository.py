from django.db import transaction
from django.db import DatabaseError
from achievement.models import PlayerAchievement, Achievement
from player.models import Player
from core.exceptions.domain import PlayerNotFoundError
from core.exceptions.bd import RepositoryError
from achievement.models import TeamAchievement
from team.models import Team
from core.exceptions.domain import TeamNotFoundError

import logging

logger = logging.getLogger(__name__)


def add_player_achievement_acquired_repository(user, achievement_code):
    try:
        with transaction.atomic():
            player = Player.objects.get(user=user)
            achievement = Achievement.objects.get(code=achievement_code)
            playerAchievement = PlayerAchievement.objects.create(
                player=player, achievement=achievement
            )
            playerAchievement.save()
            return
    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc


def add_team_achievement_acquired_repository(team_name, achievement_code):
    try:
        with transaction.atomic():
            team = Team.objects.get(name=team_name)
            achievement = Achievement.objects.get(code=achievement_code)
            teamAchievement = TeamAchievement.objects.create(
                team=team, achievement=achievement
            )
            teamAchievement.save()
            return
    except Team.DoesNotExist as exc:
        raise TeamNotFoundError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc


def player_achievement_list_repository(user):
    try:
        player = Player.objects.get(user=user)
        qs_player_achievements = PlayerAchievement.objects.filter(player=player)

        return [
            {
                "name": pa.achievement.name,
                "description": pa.achievement.description,
                "acquired_at": pa.acquired_at,
            }
            for pa in qs_player_achievements
        ]

    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc
