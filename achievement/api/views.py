from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound
from achievement.api.serializers.player_achievement_list_response_serializer import (
    PlayerAchievementResponseSerializer,
)
from achievement.api.serializers.player_achievement_acquired_request_serializer import (
    Player_Achievement_Acquired_Request_Serializer,
)
from achievement.api.serializers.player_achievement_acquired_response_serializer import (
    Player_Achievement_Acquired_Response_Serializer,
)
from achievement.api.serializers.player_team_achievement_response_serializer import (
    PlayerTeamAchievementResponseSerializer,
)
from achievement.api.serializers.team_achievement_acquired_request_serializer import (
    TeamAchievementAcquiredRequestSerializer,
)
from achievement.api.serializers.team_achievement_acquired_response_serializer import (
    TeamAchievementAcquiredResponseSerializer,
)
from achievement.api.serializers.player_achievement_list_request_serializer import (
    PlayerAchievementListRequestSerializer,
)
from achievement.api.serializers.player_team_achievement_list_request_serializer import (
    PlayerTeamAchievementListRequestSerializer,
)
from achievement.domain.services.achievement_service import (
    add_player_achievement_acquired_service,
    add_team_achievement_acquired_service,
    player_achievement_list_service,
    player_team_achievement_list_service,
)
from core.exceptions.domain import PlayerNotFoundError, TeamNotFoundError
from core.exceptions.bd import RepositoryError

import logging

logger = logging.getLogger(__name__)


class PlayerAchievementAcquireView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Player_Achievement_Acquired_Request_Serializer

    @extend_schema(
        request=Player_Achievement_Acquired_Request_Serializer,
        responses=Player_Achievement_Acquired_Response_Serializer,
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            result = add_player_achievement_acquired_service(
                user=request.user,
                achievement_code=serializer.validated_data["achievement_code"],
            )
        except PlayerNotFoundError as exc:
            raise NotFound(detail=exc.default_detail)
        response_serializer = Player_Achievement_Acquired_Response_Serializer(result)
        return Response(response_serializer.data, status=status.HTTP_200_OK)


class TeamAchievementAcquireView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamAchievementAcquiredRequestSerializer

    @extend_schema(
        request=TeamAchievementAcquiredRequestSerializer,
        responses=TeamAchievementAcquiredResponseSerializer,
    )
    def get(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = add_team_achievement_acquired_service(
            team_name=serializer.validated_data["team_name"],
            achievement_code=serializer.validated_data["achievement_code"],
        )
        response_serializer = TeamAchievementAcquiredResponseSerializer(result)
        return Response(response_serializer.data, status=status.HTTP_200_OK)


class PlayerAchievementListView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlayerAchievementListRequestSerializer

    @extend_schema(responses=PlayerAchievementResponseSerializer)
    def get(self, request):
        try:
            result = {
                "player_achievement_list": player_achievement_list_service(
                    user=request.user
                )
            }
            response_serializer = PlayerAchievementResponseSerializer(result)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        except PlayerNotFoundError as exc:
            raise NotFound(detail=exc.default_detail)
        except RepositoryError as exc:
            raise NotFound(detail=exc.default_detail)


# Shows the achievement list for a player in a specific team
class PlayerTeamAchievementListView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlayerTeamAchievementListRequestSerializer

    @extend_schema(
        request=PlayerTeamAchievementListRequestSerializer,
        responses=PlayerTeamAchievementResponseSerializer,
    )
    def get(self, request):
        logger.info("PlayerTeamAchievementListView GET request received")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        team_name = serializer.validated_data["team_name"]
        try:
            result = player_team_achievement_list_service(
                user=request.user, team_name=team_name
            )

            response_serializer = PlayerTeamAchievementResponseSerializer(result)

            return Response(response_serializer.data, status=status.HTTP_200_OK)
        except PlayerNotFoundError:
            raise
        except TeamNotFoundError:
            raise
        except RepositoryError:
            raise


class TeamAchievementListView(GenericAPIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
