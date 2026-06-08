from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions, status
from core.exceptions.bd import RepositoryError
from core.exceptions.domain import PlayerNotFoundError
from store.api.serializers.store_item_acquire_request_serializer import (
    StoreItemAcquireRequestSerializer,
)
from store.api.serializers.store_item_acquire_response_serializer import (
    StoreItemAcquireResponseSerializer,
)
from store.domain.services.store_service import (
    coins_acquire_service,
    store_item_acquire_service,
)
from store.api.serializers.coins_acquire_request_serializer import (
    CoinsAcquireRequestSerializer,
)
from store.api.serializers.coins_acquire_response_serializer import (
    CoinsAcquireResponseSerializer,
)


class CoinsAcquireAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CoinsAcquireRequestSerializer

    @extend_schema(
        request=CoinsAcquireRequestSerializer, responses=CoinsAcquireResponseSerializer
    )
    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = coins_acquire_service(
                user=request.user,
                coins_acquire_qty=serializer.validated_data["coins_acquire_qty"],
            )
            response_serializer = CoinsAcquireResponseSerializer(result)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        except PlayerNotFoundError:
            raise
        except RepositoryError:
            raise


class StoreItemAcquireAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = StoreItemAcquireRequestSerializer

    @extend_schema(
        request=StoreItemAcquireRequestSerializer,
        responses=StoreItemAcquireResponseSerializer,
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = store_item_acquire_service(
                user=request.user,
                store_item_id=serializer.validated_data["store_item_name"],
            )

            response_serializer = StoreItemAcquireResponseSerializer(result)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        except PlayerNotFoundError:
            raise
        except RepositoryError:
            raise
