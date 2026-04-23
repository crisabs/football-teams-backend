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
