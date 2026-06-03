from rest_framework import serializers


class AchievementSerializer(serializers.Serializer):
    achievement_name = serializers.CharField()
    achievement_code = serializers.CharField()
    achievement_description = serializers.CharField()
    acquired_at = serializers.DateTimeField()
    notes = serializers.CharField(allow_blank=True, required=False)


class PlayerTeamAchievementResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    achievements = AchievementSerializer(many=True, required=False)
