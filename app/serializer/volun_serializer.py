from rest_framework import serializers
from app.models import VolunList


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunList
        fields = ('id', 'title', 'subtitle', 'image_url', 'start_date', 'end_date')
