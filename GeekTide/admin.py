from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Profile

# Register your models here.
# Настройка админки для Post с использованием Summernote
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'owner', 'created_at')  # Отображение полей
    search_fields = ('title', 'description', 'tags')  # Поля для поиска
    list_filter = ('created_at', 'owner')  # Фильтрация
    summernote_fields = ('description',)  # Используем Summernote для поля description

# Настройка админки для Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'user', 'first_name', 'last_name')  # Отображение полей
    search_fields = ('nickname', 'user__username', 'first_name', 'last_name')  # Поля для поиска
    list_filter = ('user',)  # Фильтрация