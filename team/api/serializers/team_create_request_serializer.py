from rest_framework import serializers


class TeamCreateRequestSerializer(serializers.Serializer):
    team_name = serializers.CharField(max_length=50)
    team_nickname = serializers.CharField(max_length=50)
    team_slogan = serializers.CharField(max_length=50)
    team_city = serializers.CharField(max_length=50)
    team_country = serializers.CharField(max_length=50)
