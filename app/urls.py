from django.urls import path, re_path
from app.views import CardList, Co2List

urlpatterns = [
  path('cards/<str:category>/', CardList.as_view()),
  path('cards/', CardList.as_view()),
  path('co2/', Co2List.as_view())
]