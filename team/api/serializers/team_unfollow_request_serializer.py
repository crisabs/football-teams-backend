from rest_framework import serializers


class UnfollowTeamRequestSerializer(serializers.Serializer):
    team_name = serializers.CharField(max_length=100)
