from rest_framework import serializers


class TeamAcceptPlayerRequestSerializer(serializers.Serializer):
    player_request_name = serializers.CharField(max_length=100)
    team_name = serializers.CharField(max_length=100)
