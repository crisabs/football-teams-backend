from django.db import transaction, DatabaseError

from core.exceptions.bd import RepositoryError
from core.exceptions.domain import PlayerNotFoundError
from player.models import Player


def coins_acquire_repository(user, coins_acquire_qty):
    try:
        with transaction.atomic():
            player = Player.objects.select_for_update().get(user=user)
            player.coins += coins_acquire_qty
            player.save()
            return {"message": f"{player.nickname} acquired {coins_acquire_qty} coins"}
    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc
