from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializer import VolunteerSerializer
from app.enums import DAILY, EVENT
from app.models import VolunList


class VolunteerList(APIView):


    @swagger_auto_schema(
        responses={
            200: VolunteerSerializer()
        })
    def get(self, request):
        queryset = VolunList.objects.all()

        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VolunteerSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
