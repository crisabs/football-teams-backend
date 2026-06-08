from django.db import transaction, DatabaseError

from core.exceptions.bd import RepositoryError
from core.exceptions.domain import PlayerNotFoundError
from player.models import Player
from store.models import PlayerStoreItem, StoreItem


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


def store_item_acquire_repository(user, store_item_id):
    try:
        with transaction.atomic():
            player = Player.objects.get(user=user)
            store_item = StoreItem.objects.get(name=store_item_id)

            player_store_item = PlayerStoreItem.objects.create(
                player=player, store_item=store_item
            )
            player_store_item.save()
            return {"message": f"{player.nickname} acquired {store_item.name}"}
    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except StoreItem.DoesNotExist as exc:
        raise RepositoryError("Store item not found") from exc
    except DatabaseError as exc:
        raise RepositoryError from exc
