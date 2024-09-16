from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('load-posts/', views.load_posts, name='load_posts'),  # Новый URL для подгрузки постов
    path('profile/<str:nickname>/', views.profile, name='profile'),
]