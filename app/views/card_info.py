from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializer import CardListSerializer
from app.enums import DAILY, EVENT
from app.models import WarningCardInfo, SolveCardInfo


class CardList(APIView):

  def get_objects(self, category):
    try:
      if category is None:
        return WarningCardInfo.objects
      else:
        return SolveCardInfo.objects.filter(category=category)

    except CardInfo.DoesNotExist:
      return None

  @swagger_auto_schema(
    responses={
    200:CardListSerializer()
  })
  def get(self, request, category=None):
    queryset = self.get_objects(category)
  
    if queryset is None:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
    data = dict(
      cards=queryset.all(),
      count=queryset.count()
    )
    serializer = CardListSerializer(data)
    # TODO: add category, year
    
    return Response(serializer.data, status=status.HTTP_200_OK)
