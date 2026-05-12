from player.models import Player
from team.models import Role, Team, PlayerTeam, PlayerProposalTeam
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
        followers_qty = PlayerTeam.objects.filter(
            team=team, roles__name="FOLLOWER"
        ).count()
        return {
            "name": team.name,
            "nickname": team.nickname,
            "slogan": team.slogan,
            "city": team.city,
            "country": team.country,
            "foundation_date": team.foundation_date,
            "qty_followers": followers_qty,
            "players": [player.nickname for player in team.players.all()],
        }
    except DatabaseError as exc:
        raise RepositoryError from exc
    except Team.DoesNotExist:
        raise TeamNotFoundError(f"Team with name {team_name} not found")


def team_join_request_list_repository(user, team_name):
    try:

        player = Player.objects.get(user=user)
        logger.debug(
            f"Player {player.nickname} is requesting join request list for team {team_name}"
        )
        team = Team.objects.get(name=team_name)

        player_team = PlayerTeam.objects.get(player=player, team=team)
        logger.debug(f"Player {player.nickname} is a member of team {player_team.team}")

        player_team_role = (
            Role.objects.filter(playerteam=player_team)
            .values_list("name", flat=True)
            .first()
        )
        player_proposals = PlayerProposalTeam.objects.filter(team=team)
        logger.debug(
            f"Player {player.nickname} has role {player_team_role} in team {player_team.team}"
        )
        if player_team_role != "ADMIN":
            logger.warning(
                f"Player {player.nickname} does not have permission to join requests for team {team.name}"
            )
            raise PlayerWithoutPermission(
                "You do not have permission to view join requests for this team"
            )
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
