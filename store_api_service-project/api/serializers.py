from rest_framework import serializers

from api.models import Good, Token



def is_valid_token(value):
    if len(value) != 36:
        raise serializers.ValidationError("Token must be 36 characters long")
    if Token.objects.filter(token=value).exists():
        raise serializers.ValidationError("Token already exists")
    

def is_valid_amount(value):
    if value < 0:
        raise serializers.ValidationError("Amount must be more than 0")

def is_valid_price(value):
    if value < 0:
        raise serializers.ValidationError("Price must be more than 0")
    
class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=36,validators=[is_valid_token])
    
class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    amount = serializers.IntegerField(validators=[is_valid_amount])
    price = serializers.IntegerField(validators=[is_valid_price])
    
    def create(self, validated_data):
        return Good.objects.create(**validated_data)