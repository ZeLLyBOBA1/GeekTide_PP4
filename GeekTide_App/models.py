from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)  # Заголовок поста
    content = models.TextField()  # Текст поста
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с моделью пользователя
    published_at = models.DateTimeField(auto_now_add=True)  # Дата публикации (автоматически устанавливается при создании)

    def __str__(self):
        return self.title  # Для отображения заголовка поста в админке и других местах