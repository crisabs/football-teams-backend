from rest_framework import serializers


class TeamLeaveResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
