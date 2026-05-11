from rest_framework import serializers

"""class PlayerTeamDetail(serializers.Serializer):
    players = serializers.CharField()
"""


class TeamDetailResponseSerializer(serializers.Serializer):
    name = serializers.CharField()
    nickname = serializers.CharField()
    slogan = serializers.CharField()
    city = serializers.CharField()
    country = serializers.CharField()
    foundation_date = serializers.CharField()
    qty_followers = serializers.IntegerField()
    players = serializers.CharField()
