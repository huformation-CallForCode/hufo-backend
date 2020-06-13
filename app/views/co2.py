from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializer import Co2Serializer
from app.models import Co2Emission


class Co2List(APIView):
  @swagger_auto_schema(
    responses={
    200:Co2Serializer(many=True)
  })
  def get(self, request, ):
    queryset = Co2Emission.objects.all()
  
    if queryset is None:
      return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = Co2Serializer(queryset, many=True)

    data = serializer.data

    result = []
    country = []
    year = []
    country_data = {}
    for da in data:
      year.append(da['year'])
      country.append(da['country'])

      if da['country'] not in country_data.keys():
        country_data[da['country']] = [da['amount']]
      else:
        country_data[da['country']].append(da['amount'])

    result = [set(year), set(country), country_data]      

    return Response(result, status=status.HTTP_200_OK)

class Co2(APIView):
  @swagger_auto_schema(
    responses={
    200:Co2Serializer()
  })
  def get(self, request):
    query = Co2Emission.objects.filter(year=2017).filter(country='South Korea').first()

    serializer = Co2Serializer(query)
    return Response(serializer.data, status=status.HTTP_200_OK)