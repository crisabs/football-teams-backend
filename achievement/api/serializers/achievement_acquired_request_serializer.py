from rest_framework import serializers


class Achievement_Acquired_Request_Serializer(serializers.Serializer):
    achievement_code = serializers.IntegerField()
