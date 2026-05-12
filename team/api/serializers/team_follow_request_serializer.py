from rest_framework import serializers


class TeamFollowRequestSerializer(serializers.Serializer):
    team_name = serializers.CharField(max_length=100)
