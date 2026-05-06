from rest_framework import serializers


class TeamRequestResponseSerializer(serializers.Serializer):
    player = serializers.CharField()
    team = serializers.CharField()
    role = serializers.CharField()
    proposal_date = serializers.CharField()
    proposal_message = serializers.CharField()


class TeamRequestListResponseSerializer(serializers.Serializer):
    list = TeamRequestResponseSerializer(many=True)
