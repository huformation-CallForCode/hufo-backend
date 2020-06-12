from rest_framework import serializers
from app.models import WarningCardInfo


class CardInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = WarningCardInfo
    fields = ('id', 'title', 'subtitle')

class CardListSerializer(serializers.Serializer):
  cards = CardInfoSerializer(required=False, many=True)
  count = serializers.IntegerField()
