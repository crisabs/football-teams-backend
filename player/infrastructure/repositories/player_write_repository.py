from django.db import DatabaseError, transaction
from core.exceptions.bd import RepositoryError
from player.models import Player
from core.exceptions.domain import PlayerNotFoundError


def set_player_nickname_repository(user, new_nickname):
    try:
        with transaction.atomic():
            player = Player.objects.select_for_update().get(user=user)
            player.nickname = new_nickname
            player.save()
            return {"message": "Nickname updated"}
    except Player.DoesNotExist as e:
        raise PlayerNotFoundError from e
    except DatabaseError as e:
        raise RepositoryError from e


def player_gain_experience_repository(user, experience_gain):
    try:
        with transaction.atomic():
            player = Player.objects.select_for_update().get(user=user)
            player.experience += experience_gain
            player.save()
            return {"message": f"Gain {experience_gain}"}

    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc
