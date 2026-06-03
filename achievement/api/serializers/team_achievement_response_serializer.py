from rest_framework import serializers


class TeamAchievementSerializer(serializers.Serializer):
    achievement_code = serializers.CharField()
    achievement_name = serializers.CharField()
    achievement_description = serializers.CharField()
    acquired_at = serializers.DateTimeField()
    notes = serializers.CharField(allow_blank=True, required=False)


class TeamAchievementResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    achievements = TeamAchievementSerializer(many=True, required=False)
