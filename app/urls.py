from django.urls import path
from app.views import CardList, Co2List
from app.views import TemperatureList, TemperatureNow


urlpatterns = [
  path('cards/<str:category>/', CardList.as_view()),
  path('cards/', CardList.as_view()),
  path('co2/', Co2List.as_view())
  path('temperature_data/', TemperatureList.as_view()),
  path('temperature/<int:year>/', TemperatureNow.as_view())
]
