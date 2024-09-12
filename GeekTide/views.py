from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_at')  # Получаем все посты, отсортированные по дате
    return render(request, 'index.html', {'posts': posts})  # Передаем посты в шаблон