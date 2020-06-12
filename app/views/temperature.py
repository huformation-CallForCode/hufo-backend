from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializer import TemperatureSerializer
from app.models import Temperature


class TemperatureList(APIView):
  @swagger_auto_schema(
    responses={
    200:TemperatureSerializer(many=True)
  })
  def get(self, request):
    queryset = Temperature.objects.all()
  
    if queryset is None:
      return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TemperatureSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

class TemperatureNow(APIView):
  @swagger_auto_schema(
    responses={
    200:TemperatureSerializer()
  })
  def get(self, request, year):
    query = Temperature.objects.filter(year=year).first()
  
    if query is None:
      return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TemperatureSerializer(query)

    return Response(serializer.data, status=status.HTTP_200_OK)
