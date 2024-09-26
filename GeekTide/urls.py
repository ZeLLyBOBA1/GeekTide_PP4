from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),  
    path('load-posts/', views.load_posts, name='load_posts'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:display_name>/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('create/', views.create_post, name='create_post'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
]