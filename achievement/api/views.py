from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound
from achievement.api.serializers.achievement_acquired_request_serializer import (
    Achievement_Acquired_Request_Serializer,
)
from achievement.api.serializers.achievement_acquired_response_serializer import (
    Achievement_Acquired_Response_Serializer,
)
from achievement.domain.services.achievement_service import (
    add_player_achievement_acquired,
)
from core.exceptions.domain import PlayerNotFoundError


class AchievementAcquiredView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Achievement_Acquired_Request_Serializer

    @extend_schema(
        request=Achievement_Acquired_Request_Serializer,
        responses=Achievement_Acquired_Response_Serializer,
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            result = add_player_achievement_acquired(
                user=request.user, achievement_code=10
            )
        except PlayerNotFoundError as exc:
            raise NotFound(detail=exc.default_detail)
        response_serializer = Achievement_Acquired_Response_Serializer(result)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
