from rest_framework import serializers


class TeamLeaveRequestSerializer(serializers.Serializer):
    team_name = serializers.CharField(max_length=50)
