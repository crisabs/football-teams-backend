from rest_framework import serializers


class PlayerProfileImageRequestSerializer(serializers.Serializer):
    image_id = serializers.IntegerField(min_value=0, max_value=200)
