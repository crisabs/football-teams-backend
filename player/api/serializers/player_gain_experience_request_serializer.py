from rest_framework import serializers


class PlayerGainExperienceRequestSerializer(serializers.Serializer):
    experience_gain = serializers.IntegerField(min_value=1)
