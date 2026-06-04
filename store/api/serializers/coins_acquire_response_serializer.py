from rest_framework import serializers


class CoinsAcquireResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
