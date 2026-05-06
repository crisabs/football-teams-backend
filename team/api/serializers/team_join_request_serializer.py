from rest_framework import serializers


class TeamJoinRequestSerializer(serializers.Serializer):
    team_name = serializers.CharField(max_length=50)
