from rest_framework import serializers


class StoreItemAcquireResponseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
