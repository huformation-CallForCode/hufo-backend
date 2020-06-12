from rest_framework import serializers
from app.models import Co2Emission


class Co2Serializer(serializers.BaseSerializer):
  year = serializers.IntegerField()
  country = serializers.ListField(child=serializers.CharField(max_length=32))
