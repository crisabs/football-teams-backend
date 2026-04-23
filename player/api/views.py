from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from player.api.serializers.player_me_details_response_serializer import (
    PlayerMeDetailsResponseSerializer,
)
from player.api.serializers.player_nick_request_serializer import (
    PlayerNickRequestSerializer,
)
from player.api.serializers.player_nick_response_serializer import (
    PlayerNickResponseSerializer,
)
from player.api.serializers.player_profile_image_request_serializer import (
    PlayerProfileImageRequestSerializer,
)
from player.api.serializers.player_profile_image_response_serializer import (
    PlayerProfileImageResponseSerializer,
)
from player.domain.services.player_service import (
    get_player_me_details,
    set_player_nickname,
    set_player_profile_image,
)
from rest_framework import permissions
from drf_spectacular.utils import extend_schema


class PlayerMeDetailsAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(responses=PlayerMeDetailsResponseSerializer)
    def get(self, request):
        result = get_player_me_details(request.user)
        response_serializer = PlayerMeDetailsResponseSerializer(result)
        return Response(response_serializer.data, status=status.HTTP_200_OK)


class PlayerNickAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlayerNickRequestSerializer

    @extend_schema(
        request=PlayerNickRequestSerializer, responses=PlayerNickResponseSerializer
    )
    def patch(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_nickname = serializer.validated_data["new_nickname"]

        result = set_player_nickname(user=request.user, new_nickname=new_nickname)
        response_serializer = PlayerNickResponseSerializer(result)
        return Response(response_serializer.data, status=status.HTTP_200_OK)


class PlayerProfileImage(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlayerProfileImageRequestSerializer

    @extend_schema(
        request=PlayerProfileImageRequestSerializer,
        responses=PlayerProfileImageResponseSerializer,
    )
    def patch(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_id = serializer.validated_data["image_id"]
        result = set_player_profile_image(user=request.user, image_id=image_id)
        response_serializer = PlayerProfileImageResponseSerializer(result)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
