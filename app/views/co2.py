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

    return Response(serializer.data, status=status.HTTP_200_OK)
