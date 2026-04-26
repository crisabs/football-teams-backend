from rest_framework import serializers


class Achievement_Acquired_Response_Serializer(serializers.Serializer):
    message = serializers.CharField()
