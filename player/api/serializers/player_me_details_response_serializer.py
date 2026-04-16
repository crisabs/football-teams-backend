from rest_framework import serializers


class TeamResponseSerializer(serializers.Serializer):
    team = serializers.CharField()


class AchievementResponseSerializer(serializers.Serializer):
    achievement = serializers.CharField()


class PlayerMeDetailsResponseSerializer(serializers.Serializer):
    nickname = serializers.CharField()
    level = serializers.IntegerField()
    exp = serializers.IntegerField()
    coins = serializers.IntegerField(min_value=0)
    teams = TeamResponseSerializer(many=True)
    achievements = AchievementResponseSerializer(many=True)
