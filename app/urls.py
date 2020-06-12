from django.urls import path, re_path
from app.views import CardList
from app.views import VolunteerList

urlpatterns = [
    path('cards/<str:category>/', CardList.as_view()),
    path('cards/', CardList.as_view()),
    path('volunteers/', VolunteerList.as_view())
]
