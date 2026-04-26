from achievement.infrastructure.achievement_write_repository import (
    add_player_achievement_acquired_repository,
)
from core.exceptions.bd import RepositoryError
from core.exceptions.domain import PlayerNotFoundError


def add_player_achievement_acquired(user, achievement_code):
    try:
        add_player_achievement_acquired_repository(
            user=user, achievement_code=achievement_code
        )
        return {"message": f"Felicidades has alcanzado el logro de {achievement_code}"}
    except PlayerNotFoundError:
        raise
    except RepositoryError:
        raise
