from rest_framework import serializers


class TeamFollowResponseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
