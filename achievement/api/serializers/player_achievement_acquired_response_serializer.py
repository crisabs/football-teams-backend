from rest_framework import serializers


class Player_Achievement_Acquired_Response_Serializer(serializers.Serializer):
    message = serializers.CharField()
