from core.exceptions.bd import RepositoryError
from core.exceptions.domain import (
    PlayerNotFoundError,
    TeamNotFoundError,
    PlayerWithoutPermission,
)
from team.infrastructure.repositories.team_write_repository import (
    create_team_service_repository,
    join_request_into_team_repository,
    team_leave_repository,
    team_accept_join_request_repository,
)
from team.infrastructure.repositories.team_read_repository import (
    get_team_details_service_repository,
    team_join_request_list_repository,
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


def join_request_into_team(user, team_name):
    try:
        return join_request_into_team_repository(user=user, team_name=team_name)
    except RepositoryError:
        logger.exception("Repository error on join request into team")
        raise
    except TeamNotFoundError:
        logger.exception("TeamNotFoundError on join request into team")
        raise
    except PlayerNotFoundError:
        logger.exception("PlayerNotFoundError on join request into team")
        raise


def team_join_request_list_service(user, team_name):
    try:
        result = team_join_request_list_repository(user=user, team_name=team_name)
        logger.info(f"list result --> {result}")
        return result
    except PlayerNotFoundError:
        logger.exception("PlayerNotFoundError on join list request")
        raise
    except RepositoryError:
        logger.exception("Repository error on join list request")
        raise
    except PlayerWithoutPermission:
        logger.exception("PlayerWithoutPermission on list request")
        raise


def team_leave_service(user, team_name):
    return team_leave_repository(user=user, team_name=team_name)


def team_accept_join_request_service(user, player_request_name, team_name):
    try:
        return team_accept_join_request_repository(
            user=user, player_request_name=player_request_name, team_name=team_name
        )
    except RepositoryError:
        raise
    except TeamNotFoundError:
        raise
    except PlayerNotFoundError:
        raise
