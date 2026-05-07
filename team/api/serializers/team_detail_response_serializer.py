from rest_framework import serializers


class PlayerTeamDetail(serializers.Serializer):
    player_name = serializers.CharField()


class TeamDetailResponseSerializer(serializers.Serializer):
    name = serializers.CharField()
    nickname = serializers.CharField()
    slogan = serializers.CharField()
    city = serializers.CharField()
    country = serializers.CharField()
    foundation_date = serializers.CharField()
    followers_count = serializers.IntegerField()
    players = PlayerTeamDetail(many=True)
