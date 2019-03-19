from rest_framework import serializers
from api.models import Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('name', 'symbol', 'icon')