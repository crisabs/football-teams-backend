from rest_framework import serializers


class PlayerAchievementSerializer(serializers.Serializer):
    name = serializers.CharField()
    acquired_at = serializers.CharField()
    description = serializers.CharField()


class PlayerAchievementResponseSerializer(serializers.Serializer):
    player_achievement_list = PlayerAchievementSerializer(many=True)
