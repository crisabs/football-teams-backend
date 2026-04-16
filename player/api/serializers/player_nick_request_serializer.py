from rest_framework import serializers
from django.core.validators import RegexValidator


class PlayerNickRequestSerializer(serializers.Serializer):
    new_nickname = serializers.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^[A-Za-z0-9_]+$",
                message="Nickname can only contain letters, numbers, and underscores.",
            )
        ],
        trim_whitespace=True,
    )
