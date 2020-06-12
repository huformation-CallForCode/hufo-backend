from django.urls import path, re_path
from app.views import CardList

urlpatterns = [
  path('cards/<str:category>/', CardList.as_view()),
  path('cards/', CardList.as_view())
]