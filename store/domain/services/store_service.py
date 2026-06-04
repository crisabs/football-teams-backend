from core.exceptions.bd import RepositoryError
from core.exceptions.domain import PlayerNotFoundError
from store.infrastructure.repositories.write_store_repository import (
    coins_acquire_repository,
)


def coins_acquire_service(user, coins_acquire_qty):
    try:
        return coins_acquire_repository(user=user, coins_acquire_qty=coins_acquire_qty)
    except PlayerNotFoundError:
        raise
    except RepositoryError:
        raise
