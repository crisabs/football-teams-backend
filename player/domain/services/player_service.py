from core.exceptions.bd import RepositoryError
from core.exceptions.domain import PlayerNotFoundError
from player.infrastructure.repositories.player_read_repository import (
    get_player_me_details_repository,
)
from player.infrastructure.repositories.player_write_repository import (
    set_player_nickname_repository,
)

import logging

logger = logging.getLogger(__name__)


def get_player_me_details(user):
    try:
        return get_player_me_details_repository(user=user)
    except PlayerNotFoundError:
        logger.exception("No Player profile associated with retrieving player details")
        raise
    except RepositoryError:
        logger.exception("Repository failure while retrieving player details")
        raise


def set_player_nickname(user, new_nickname):
    try:
        result = set_player_nickname_repository(user=user, new_nickname=new_nickname)
        return result
    except PlayerNotFoundError:
        logger.exception(
            "No Player profile associated with user while updating the nickname"
        )
        raise
    except RepositoryError:
        logger.exception("Repository failure while updating player nickname")
        raise


def set_player_profile_image(user, image_id):
    return {"message": "Player profile image updated"}
