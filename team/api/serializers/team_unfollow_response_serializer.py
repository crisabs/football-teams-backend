from rest_framework import serializers


class UnfollowTeamResponseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
