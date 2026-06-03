from achievement.infrastructure.achievement_write_repository import (
    add_player_achievement_acquired_repository,
    add_team_achievement_acquired_repository,
    player_achievement_list_repository,
)
from achievement.infrastructure.achievement_read_repository import (
    player_team_achievement_list_repository,
    team_achievement_list_repository,
)
from core.exceptions.bd import RepositoryError
from core.exceptions.domain import PlayerNotFoundError, TeamNotFoundError


def add_player_achievement_acquired_service(user, achievement_code):
    try:
        add_player_achievement_acquired_repository(
            user=user, achievement_code=achievement_code
        )
        return {"message": f"Felicidades has alcanzado el logro de {achievement_code}"}
    except PlayerNotFoundError:
        raise
    except RepositoryError:
        raise


def add_team_achievement_acquired_service(team_name, achievement_code):
    try:
        add_team_achievement_acquired_repository(
            team_name=team_name, achievement_code=achievement_code
        )
        return {"message": f" {team_name} got {achievement_code} achievement"}
    except TeamNotFoundError:
        raise
    except RepositoryError:
        raise


def player_achievement_list_service(user):
    try:
        return player_achievement_list_repository(user=user)
    except PlayerNotFoundError:
        raise
    except RepositoryError:
        raise


def player_team_achievement_list_service(user, team_name):
    try:
        return player_team_achievement_list_repository(user=user, team_name=team_name)
    except PlayerNotFoundError:
        raise
    except TeamNotFoundError:
        raise
    except RepositoryError:
        raise


def team_achievement_list_service(team_name):
    try:
        return team_achievement_list_repository(team_name=team_name)
    except TeamNotFoundError:
        raise
    except RepositoryError:
        raise
