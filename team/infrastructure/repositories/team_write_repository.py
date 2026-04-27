from django.db import transaction, DatabaseError
from core.exceptions.bd import RepositoryError
from core.exceptions.domain import PlayerNotFoundError
from team.models import Team
from player.models import Player


def create_team_service_repository(
    user, team_name, team_nickname, team_slogan, team_city, team_country
):
    try:
        with transaction.atomic():
            player = Player.objects.get(user=user)
            team = Team.objects.create(
                name=team_name,
                nickname=team_nickname,
                slogan=team_slogan,
                city=team_city,
                country=team_country,
                founder=player,
            )
            team.save()
    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc
