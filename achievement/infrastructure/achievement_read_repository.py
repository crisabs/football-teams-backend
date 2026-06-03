from achievement.models import PlayerTeamAchievement
from core.exceptions.bd import RepositoryError
from core.exceptions.domain import (
    PlayerNotFoundError,
    TeamNotFoundError,
    PlayerTeamAchievementNotFoundError,
)
from django.db import DatabaseError
from player.models import Player
from team.models import Team


def player_team_achievement_list_repository(user, team_name):
    try:
        player = Player.objects.get(user=user)
        team = Team.objects.get(name=team_name)

        player_team_achievements = (
            PlayerTeamAchievement.objects.filter(player=player, team=team)
            .select_related("achievement")
            .order_by("-acquired_at")
        )
        if not player_team_achievements.exists():

            return {"message": "No achievements found for this player and team."}

        return {
            "message": "Achievements retrieved successfully.",
            "achievements": [
                {
                    "achievement_name": pta.achievement.name,
                    "achievement_code": pta.achievement.code,
                    "description": pta.achievement.description,
                    "acquired_at": pta.acquired_at,
                    "notes": pta.notes,
                }
                for pta in player_team_achievements
            ],
        }
    except Player.DoesNotExist as exc:
        raise PlayerNotFoundError from exc
    except Team.DoesNotExist as exc:
        raise TeamNotFoundError from exc
    except PlayerTeamAchievement.DoesNotExist as exc:
        raise PlayerTeamAchievementNotFoundError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc


def team_achievement_list_repository(team_name):
    try:
        team = Team.objects.get(name=team_name)

        team_achievements = (
            PlayerTeamAchievement.objects.filter(team=team)
            .select_related("achievement")
            .order_by("-acquired_at")
        )
        if not team_achievements.exists():
            return {"message": "No achievements found for this team."}

        return {
            "message": "Achievements retrieved successfully.",
            "achievements": [
                {
                    "achievement_name": ta.achievement.name,
                    "achievement_code": ta.achievement.code,
                    "description": ta.achievement.description,
                    "acquired_at": ta.acquired_at,
                    "notes": ta.notes,
                }
                for ta in team_achievements
            ],
        }
    except Team.DoesNotExist as exc:
        raise TeamNotFoundError from exc
    except PlayerTeamAchievement.DoesNotExist as exc:
        raise PlayerTeamAchievementNotFoundError from exc
    except DatabaseError as exc:
        raise RepositoryError from exc
