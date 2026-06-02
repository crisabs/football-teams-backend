from rest_framework import serializers


class TeamAchievementAcquiredResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
