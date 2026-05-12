from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from drf_spectacular.utils import extend_schema
from core.exceptions.bd import RepositoryError
from core.exceptions.domain import (
    PlayerNotFoundError,
    PlayerTeamNotFoundError,
    PlayerWithoutPermission,
    TeamNotFoundError,
)
from team.api.serializers.team_accept_player_request_serializer import (
    TeamAcceptPlayerRequestSerializer,
)
from team.api.serializers.team_accept_player_response_serializer import (
    TeamAcceptPlayerResponseSerializer,
)
from team.api.serializers.team_delete_request_serializer import (
    TeamDeleteRequestSerializer,
)
from team.api.serializers.team_delete_response_serializer import (
    TeamDeleteResponseSerializer,
)
from team.api.serializers.team_follow_request_serializer import (
    TeamFollowRequestSerializer,
)
from team.api.serializers.team_detail_request_serializer import (
    TeamDetailRequestSerializer,
)
from team.api.serializers.team_detail_response_serializer import (
    TeamDetailResponseSerializer,
)
from team.api.serializers.team_follow_response_serializer import (
    TeamFollowResponseSerializer,
)
from team.api.serializers.team_join_request_serializer import TeamJoinRequestSerializer
from team.api.serializers.team_leave_request_serializer import (
    TeamLeaveRequestSerializer,
)
from team.api.serializers.team_leave_response_serializer import (
    TeamLeaveResponseSerializer,
)
from team.api.serializers.team_request_list_request_serializer import (
    TeamRequestListRequestSerializer,
)
from team.api.serializers.team_request_list_response_serializer import (
    TeamRequestListResponseSerializer,
)
from team.domain.services.team_service import (
    create_team_service,
    get_team_details_service,
    join_request_into_team,
    team_join_request_list_service,
    team_leave_service,
    team_accept_join_request_service,
    team_delete_service,
    team_follow_service,
    team_unfollow_service,
)
from team.api.serializers.team_create_request_serializer import (
    TeamCreateRequestSerializer,
)


class TeamCreateAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamCreateRequestSerializer

    @extend_schema(request=TeamCreateRequestSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            result = create_team_service(
                user=request.user,
                team_name=serializer.validated_data["team_name"],
                team_nickname=serializer.validated_data["team_nickname"],
                team_slogan=serializer.validated_data["team_slogan"],
                team_city=serializer.validated_data["team_city"],
                team_country=serializer.validated_data["team_country"],
            )
        except PlayerNotFoundError as exc:
            raise NotFound(detail=str(exc)) from exc
        return Response(result, status=status.HTTP_201_CREATED)


class TeamDetailAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamDetailRequestSerializer

    @extend_schema(
        request=TeamDetailRequestSerializer, responses=TeamDetailResponseSerializer
    )
    def get(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            result = get_team_details_service(
                team_name=serializer.validated_data["team_name"]
            )
            response_serializer = TeamDetailResponseSerializer(result)

            return Response(response_serializer.data, status=status.HTTP_200_OK)
        except TeamNotFoundError as exc:
            raise NotFound(detail=str(exc)) from exc


class TeamListAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Team list endpoint"}, status=status.HTTP_200_OK)


class TeamJoinRequestAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamJoinRequestSerializer

    @extend_schema(request=TeamJoinRequestSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = join_request_into_team(
                user=request.user, team_name=serializer.validated_data["team_name"]
            )
            return Response(result, status=status.HTTP_200_OK)
        except TeamNotFoundError as exc:
            raise NotFound(detail=str(exc)) from exc
        except PlayerNotFoundError as exc:
            raise NotFound(detail=str(exc)) from exc


class TeamJoinRequestListAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamRequestListRequestSerializer

    @extend_schema(
        request=TeamRequestListRequestSerializer,
        responses=TeamRequestListResponseSerializer,
    )
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = {
            "list": team_join_request_list_service(
                user=request.user, team_name=serializer.validated_data["team_name"]
            )
        }

        response_serializer = TeamRequestListResponseSerializer(result)

        try:
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        except PlayerNotFoundError:
            raise
        except RepositoryError:
            raise
        except PlayerWithoutPermission:
            raise


class TeamLeaveAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamLeaveRequestSerializer

    @extend_schema(
        request=TeamLeaveRequestSerializer, responses=TeamLeaveResponseSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = team_leave_service(
                user=request.user, team_name=serializer.validated_data["team_name"]
            )
            response_serializer = TeamLeaveResponseSerializer(result)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        except PlayerNotFoundError:
            raise
        except TeamNotFoundError:
            raise


class TeamAcceptPlayerJoinRequestAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = TeamAcceptPlayerRequestSerializer

    @extend_schema(
        request=TeamAcceptPlayerRequestSerializer,
        responses=TeamAcceptPlayerResponseSerializer,
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            result = {
                "message": team_accept_join_request_service(
                    user=request.user,
                    player_request_name=serializer.validated_data[
                        "player_request_name"
                    ],
                    team_name=serializer.validated_data["team_name"],
                )
            }

            response_serializer = TeamAcceptPlayerResponseSerializer(result)

            return Response(response_serializer.data, status=status.HTTP_200_OK)
        except PlayerNotFoundError:
            raise
        except TeamNotFoundError:
            raise


class TeamDeleteAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamDeleteRequestSerializer

    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = {
                "message": team_delete_service(
                    user=request.user, team_name=serializer.validated_data["team_name"]
                )
            }
            response_serializer = TeamDeleteResponseSerializer(result)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        except PlayerNotFoundError:
            raise
        except TeamNotFoundError:
            raise
        except PlayerTeamNotFoundError:
            raise


class TeamFollowAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamFollowRequestSerializer

    @extend_schema(
        request=TeamFollowRequestSerializer, responses=TeamFollowResponseSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = team_follow_service(
            user=request.user, team_name=serializer.validated_data["team_name"]
        )

        response_serializer = TeamFollowResponseSerializer(result)

        return Response(response_serializer.data, status=status.HTTP_200_OK)


class TeamUnfollowAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        result = team_unfollow_service(
            user=request.user, team_name=request.data.get("team_name")
        )
        return Response(result, status=status.HTTP_200_OK)
