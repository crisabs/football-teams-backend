from team.models import Team
from core.exceptions.domain import TeamNotFoundError
from django.db import DatabaseError
from core.exceptions.bd import RepositoryError


def get_team_details_service_repository(team_name):
    try:
        team = Team.objects.get(name=team_name)
        return {
            "name": team.name,
            "nickname": team.nickname,
            "slogan": team.slogan,
            "city": team.city,
            "country": team.country,
            "foundation_date": team.foundation_date,
            "followers_count": team.followers.count(),
            "players": [player.user.nickname for player in team.players.all()],
        }
    except DatabaseError as exc:
        raise RepositoryError from exc
    except Team.DoesNotExist:
        raise TeamNotFoundError(f"Team with name {team_name} not found")
