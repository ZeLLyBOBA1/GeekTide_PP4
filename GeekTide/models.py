from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Владелец поста (ссылка на пользователя)
    title = models.CharField(max_length=200)  # Название поста
    description = models.TextField()  # Описание поста
    image = CloudinaryField('image', blank=True, null=True)  # Картинка поста (хранится в Cloudinary)
    tags = models.CharField(max_length=200, help_text="Введите теги через запятую")  # Теги для поста
    created_at = models.DateTimeField(auto_now_add=True)  # Дата публикации поста

    def __str__(self):
        return self.title

    def get_tags_list(self):
        """Разбиваем теги на список, разделяя их по запятой."""
        return self.tags.split(",")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Ссылка на встроенного пользователя Django
    nickname = models.CharField(max_length=50, unique=True)  # Никнейм пользователя
    first_name = models.CharField(max_length=100, blank=True, null=True)  # Имя пользователя
    last_name = models.CharField(max_length=100, blank=True, null=True)  # Фамилия пользователя
    bio = models.TextField(blank=True, null=True)  # Описание профиля
    avatar = CloudinaryField('image', blank=True, null=True, default='default_avatar.png')  # Аватарка пользователя

    def __str__(self):
        return self.nickname