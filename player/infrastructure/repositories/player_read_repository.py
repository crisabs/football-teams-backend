from core.exceptions.domain import PlayerNotFoundError
from player.models import Player
from django.db import DatabaseError

from team.models import PlayerTeam


def get_player_me_details_repository(user):
    try:
        player = Player.objects.get(user=user)
        playerTeam = PlayerTeam.objects.filter(player=player).select_related("team")
        return {
            "nickname": player.nickname,
            "level": player.level,
            "exp": player.experience,
            "coins": player.coins,
            "teams": [
                {
                    "name": playerTeam.team.name,
                    "nickname": playerTeam.team.nickname,
                    "role": playerTeam.roles.name,
                    "slogan": playerTeam.team.slogan,
                    "city": playerTeam.team.city,
                    "country": playerTeam.team.country,
                }
                for playerTeam in playerTeam.all()
            ],
            "achievements": [
                {"achievement": "Primer premio regional"},
                {"achievement": "El inicio de un pive"},
            ],
        }
    except Player.DoesNotExist as e:
        raise PlayerNotFoundError from e
    except DatabaseError as e:
        raise e
