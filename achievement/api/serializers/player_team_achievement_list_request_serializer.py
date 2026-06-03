from rest_framework import serializers


class PlayerTeamAchievementListRequestSerializer(serializers.Serializer):
    team_name = serializers.CharField()
