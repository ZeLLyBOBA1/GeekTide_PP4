from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)  
    description = models.TextField()  
    image = CloudinaryField('image', blank=True, null=True)  
    tags = models.CharField(max_length=200, help_text="Введите теги через запятую")  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title

    def get_tags_list(self):
        """Разбиваем теги на список, разделяя их по запятой."""
        return self.tags.split(",")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    display_name = models.CharField(max_length=50, unique=True) 
    first_name = models.CharField(max_length=100, blank=True, null=True) 
    last_name = models.CharField(max_length=100, blank=True, null=True) 
    bio = models.TextField(blank=True, null=True) 
    avatar = CloudinaryField('image', blank=True, null=True)  

    def __str__(self):
        return self.display_name