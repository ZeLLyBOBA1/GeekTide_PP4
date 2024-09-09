from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Замените на ваши маршруты и представления
]
