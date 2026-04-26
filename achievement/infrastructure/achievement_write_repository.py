from django.db import transaction
from django.db import DatabaseError
from achievement.models import PlayerAchievement, Achievement
from player.models import Player
from core.exceptions.domain import PlayerNotFoundError
from core.exceptions.bd import RepositoryError


def add_player_achievement_acquired_repository(user, achievement_code):
    try:
        with transaction.atomic():
            player = Player.objects.get(user=user)
            achievement = Achievement.objects.get(code=achievement_code)
            playerAchievement = PlayerAchievement.objects.create(
                player=player,
                achievement=achievement,
                description=achievement.description,
            )
            playerAchievement.save()
            return
    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc
