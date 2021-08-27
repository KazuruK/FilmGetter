from django.urls import path, include
from . import views

urlpatterns = [
    path('api/v1/prices/<int:kinopoisk_id>/', views.get_film),
]
