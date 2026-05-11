from django.db import transaction, DatabaseError
from core.exceptions.bd import RepositoryError
from core.exceptions.domain import (
    PlayerNotFoundError,
    PlayerTeamNotFoundError,
    TeamNotFoundError,
)
from team.models import PlayerTeamRole, Team, Role
from player.models import Player
from team.models import PlayerProposalTeam
from team.models import PlayerTeam

import logging

logger = logging.getLogger(__name__)


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
            player_team = PlayerTeam.objects.create(
                player=player, team=team, role="ADMIN"
            )
            player_team.save()

    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc


def join_request_into_team_repository(user, team_name):
    try:
        with transaction.atomic():
            player = Player.objects.get(user=user)
            team = Team.objects.get(name=team_name)
            player_proposal = PlayerProposalTeam.objects.create(
                player=player,
                team=team,
            )
            player_proposal.save()
            return {"message": f"Peticion para unirse al equipo {team_name} enviada"}
    except DatabaseError as exc:
        raise RepositoryError from exc
    except Team.DoesNotExist as exc:
        raise TeamNotFoundError from exc
    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc


def team_leave_repository(user, team_name):
    try:
        with transaction.atomic():
            player = Player.objects.get(user=user)
            team = Team.objects.get(name=team_name)
            playerTeam = PlayerTeam.objects.get(player=player, team=team)
            playerTeam.delete()
            return {"message": f"You left {team.name} team"}
    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except Team.DoesNotExist as exc:
        raise TeamNotFoundError from exc
    except PlayerTeam.DoesNotExist as exc:
        raise PlayerTeamNotFoundError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc


def team_accept_join_request_repository(user, player_request_name, team_name):
    try:
        with transaction.atomic():
            my_player = Player.objects.get(user=user)

            if not PlayerTeam.objects.filter(player=my_player, role="ADMIN").exists():
                raise RepositoryError(
                    "Player does not have permission to accept join requests"
                )

            player_request = Player.objects.get(user__username=player_request_name)

            team = Team.objects.get(name=team_name)

            if not PlayerProposalTeam.objects.filter(
                player=player_request, team=team
            ).exists():
                raise RepositoryError(
                    f"No join request found for player {player_request_name} in team {team_name}"
                )
            playerTeam = PlayerTeam.objects.create(
                player=player_request, team=team, role="PLAYER"
            )
            playerTeam.save()
            PlayerProposalTeam.objects.filter(player=player_request, team=team).delete()

            return {"message": "Team accept join request endpoint"}
    except DatabaseError as exc:
        raise RepositoryError from exc
    except Team.DoesNotExist as exc:
        raise TeamNotFoundError from exc
    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc


def team_delete_repository(user, team_name):
    """
    GIVEN a user with a Player profile and a PlayerTeam profile for the team
    WHEN user has ADMIN role and a team_name
    THEN delete the team
    """
    try:
        my_player = Player.objects.get(user=user)
        team = Team.objects.get(name=team_name)
        membership = PlayerTeam.objects.get(player=my_player, team=team)

        if not membership.roles == "ADMIN":
            return "Current player has not the permissions for this action"

        with transaction.atomic():
            team.delete()
            return f"{team_name} deleted"

    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except Team.DoesNotExist as exc:
        raise TeamNotFoundError from exc
    except PlayerTeam.DoesNotExist as exc:
        raise PlayerTeamNotFoundError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc


def team_follow_repository(user, team_name):
    """

    GIVEN a user with a Player profile and a team_name
    WHEN user is not already following the team
    THEN add the team to the player's followed teams"""
    try:
        player = Player.objects.get(user=user)
        team = Team.objects.get(name=team_name)

        logger.debug(f"Attempting to follow team: {team_name}")

        membership = PlayerTeam.objects.filter(player=player, team=team).first()

        logger.debug(f"Existing player-team relationship: {membership}")

        if membership:
            raise RepositoryError("Player is already following the team")

        with transaction.atomic():
            follower_role = Role.objects.get(name=PlayerTeamRole.FOLLOWER)

            membership = PlayerTeam.objects.create(player=player, team=team)

            membership.roles.add(follower_role)

            team.qty_followers += 1
            team.save(update_fields=["qty_followers"])
        return {"message": f"You are now following {team_name} team"}
    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except Team.DoesNotExist as exc:
        raise TeamNotFoundError from exc
    except RepositoryError as exc:
        raise RepositoryError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc
