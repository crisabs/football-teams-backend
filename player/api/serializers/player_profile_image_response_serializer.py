from rest_framework import serializers


class PlayerProfileImageResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
