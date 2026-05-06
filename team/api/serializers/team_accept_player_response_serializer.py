from rest_framework import serializers


class TeamAcceptPlayerResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
