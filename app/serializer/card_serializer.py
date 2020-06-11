from rest_framework import serializers
from app.models import CardInfo
from app.enums import POSITIVE_CHOICES


class CardInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = CardInfo
    fields = ('id', 'title', 'subtitle', 'category')

class CardListSerializer(serializers.Serializer):
  cards = CardInfoSerializer(required=False, many=True)
  count = serializers.IntegerField()

class CardRequestSerializer(serializers.Serializer):
  year = serializers.IntegerField()
  category = serializers.ChoiceField(choices=POSITIVE_CHOICES)
