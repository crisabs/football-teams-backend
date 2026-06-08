from rest_framework import serializers


class StoreItemAcquireRequestSerializer(serializers.Serializer):
    store_item_name = serializers.CharField(max_length=255)
