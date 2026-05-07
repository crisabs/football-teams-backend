from rest_framework import serializers


class TeamDeleteResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
