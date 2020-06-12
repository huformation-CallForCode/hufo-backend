from django.urls import path, re_path
from app.views import CardList
from app.views import TemperatureList, TemperatureNow

urlpatterns = [
  path('cards/<str:category>/', CardList.as_view()),
  path('cards/', CardList.as_view()),
  path('temperature_data/', TemperatureList.as_view()),
  path('temperature/<int:year>/', TemperatureNow.as_view())
]
