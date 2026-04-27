from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from drf_spectacular.utils import extend_schema
from core.exceptions.domain import PlayerNotFoundError
from team.domain.services.team_service import create_team_service
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
