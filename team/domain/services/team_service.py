from core.exceptions.bd import RepositoryError
from core.exceptions.domain import PlayerNotFoundError, TeamNotFoundError
from team.infrastructure.repositories.team_write_repository import (
    create_team_service_repository,
)
from team.infrastructure.repositories.team_read_repository import (
    get_team_details_service_repository,
)

import logging

logger = logging.getLogger(__name__)


def create_team_service(
    user, team_name, team_nickname, team_slogan, team_city, team_country
):
    try:
        create_team_service_repository(
            user=user,
            team_name=team_name,
            team_nickname=team_nickname,
            team_slogan=team_slogan,
            team_city=team_city,
            team_country=team_country,
        )
        return {"message": f"Team {team_name} created"}
    except PlayerNotFoundError:
        raise
    except RepositoryError:
        raise


def get_team_details_service(team_name):
    try:
        return get_team_details_service_repository(team_name=team_name)
    except TeamNotFoundError:
        logger.exception(TeamNotFoundError.default_detail)
        raise
    except RepositoryError:
        logger.exception(RepositoryError.default_detail)
        raise
