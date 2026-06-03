from rest_framework import serializers


class TeamAchievementRequestSerializer(serializers.Serializer):
    team_name = serializers.CharField()
