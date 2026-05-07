from player.models import Player
from team.models import Team, PlayerTeam, PlayerProposalTeam
from core.exceptions.domain import (
    PlayerNotFoundError,
    TeamNotFoundError,
    PlayerWithoutPermission,
)
from django.db import DatabaseError, IntegrityError
from core.exceptions.bd import RepositoryError

import logging

logger = logging.getLogger(__name__)


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
            "followers_count": team.followers,
            "players": [player.user.nickname for player in team.players.all()],
        }
    except DatabaseError as exc:
        raise RepositoryError from exc
    except Team.DoesNotExist:
        raise TeamNotFoundError(f"Team with name {team_name} not found")


def team_join_request_list_repository(user, team_name):
    try:

        player = Player.objects.get(user=user)
        player_team = PlayerTeam.objects.get(player=player)

        team = Team.objects.get(name=team_name)

        player_team_role = player_team.role
        player_proposals = PlayerProposalTeam.objects.filter(team=team)
        logger.debug(
            f"Player {player.nickname} has role {player_team_role} in team {player_team.team}"
        )
        if player_team_role == "ADMIN":
            return [
                {
                    "player": proposal.player.nickname,
                    "team": proposal.team.name,
                    "role": proposal.role,
                    "proposal_date": proposal.proposal_date,
                    "proposal_message": proposal.proposal_message,
                }
                for proposal in player_proposals.all()
            ]
    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except IntegrityError as exc:
        raise PlayerWithoutPermission from exc
    except DatabaseError as exc:
        raise RepositoryError from exc
