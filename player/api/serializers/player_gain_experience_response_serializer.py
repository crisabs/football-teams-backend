from rest_framework import serializers


class PlayerGainExperienceResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
