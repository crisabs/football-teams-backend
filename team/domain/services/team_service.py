from core.exceptions.bd import RepositoryError
from core.exceptions.domain import PlayerNotFoundError
from team.infrastructure.repositories.team_write_repository import (
    create_team_service_repository,
)


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
