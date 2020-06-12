from rest_framework import serializers
from app.models import Co2Emission


class Co2Serializer(serializers.ModelSerializer):
  class Meta:
    model = Co2Emission
    fields = ('country', 'year', 'amount')