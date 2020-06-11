from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializer import CardListSerializer, CardRequestSerializer
from app.enums import POSITIVE_CHOICES
from app.models import CardInfo


class CardList(APIView):

  def get_objects(self, is_positive, category, year):
    try:
      return CardInfo.objects.filter(is_positive=is_positive)
    except CardInfo.DoesNotExist:
      return None

  param_category_hint = openapi.Parameter(
    'category',
    openapi.IN_QUERY,
    description='card\'s category',
    type=openapi.TYPE_STRING,
    enum=POSITIVE_CHOICES
  )
  param_year_hint = openapi.Parameter(
    'year',
    openapi.IN_QUERY,
    description='select year',
    type=openapi.TYPE_INTEGER
  )
  @swagger_auto_schema(
    manual_parameters=[param_category_hint, param_year_hint],
    responses={
    200:CardListSerializer()
  })
  def get(self, request):
    category = self.request.query_params.get('category')
    year = self.request.query_params.get('year')
    
    queryset = self.get_objects(True, category, year)
  
    if queryset is None:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
    data = dict(
      cards=queryset.all(),
      count=queryset.count()
    )

    serializer = CardListSerializer(data)
    # TODO: add category, year
    
    return Response(serializer.data, status=status.HTTP_200_OK)
