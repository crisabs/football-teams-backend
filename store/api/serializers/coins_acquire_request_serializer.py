from rest_framework import serializers


class CoinsAcquireRequestSerializer(serializers.Serializer):
    coins_acquire_qty = serializers.IntegerField(min_value=1)
