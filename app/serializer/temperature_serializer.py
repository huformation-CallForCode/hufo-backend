from rest_framework import serializers
from app.models import Temperature


class TemperatureSerializer(serializers.ModelSerializer):
  class Meta:
    model = Temperature
    fields = ('id', 'year', 'no_smooth', 'lowess')
