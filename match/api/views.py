from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from match.domain.services.match_service import (
    match_create_service,
    match_list_service,
    match_update_service,
    match_detail_service,
)


class MatchViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        result = match_create_service()
        return Response(result, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        result = match_update_service()
        return Response(result, status=status.HTTP_200_OK)

    def list(self, request):
        result = match_list_service()
        return Response(result, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        result = match_detail_service(pk)
        return Response(result, status=status.HTTP_200_OK)
