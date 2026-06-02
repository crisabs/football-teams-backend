from rest_framework import serializers


class TeamAchievementAcquiredRequestSerializer(serializers.Serializer):
    team_name = serializers.CharField()
