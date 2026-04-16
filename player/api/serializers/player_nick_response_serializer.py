from rest_framework import serializers


class PlayerNickResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
