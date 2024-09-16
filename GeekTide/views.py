from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Profile
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # Это представление для начальной загрузки страницы
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 10)  # Показываем по 2 поста на странице

    page_number = request.GET.get('page') or 1
    posts = paginator.get_page(page_number)

    return render(request, 'index.html', {'posts': posts})

def load_posts(request):
    # Это представление для AJAX-запросов (динамическая подгрузка постов)
    page_number = request.GET.get('page')  # Получаем номер страницы из запроса
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 10)

    try:
        posts = paginator.get_page(page_number)
    except:
        posts = []

    # Формируем данные для ответа в формате JSON
    posts_data = []
    for post in posts:
        posts_data.append({
            'title': post.title,
            'description': post.description,
            'image_url': post.image.url if post.image else None,
            'owner': post.owner.username,
            'created_at': post.created_at.strftime('%Y-%m-%d'),
            'tags': post.get_tags_list(),
        })

    return JsonResponse({
        'posts': posts_data,
        'has_next': posts.has_next(),
    })

def profile(request, nickname):
    user_profile = get_object_or_404(Profile, nickname=nickname)
    return render(request, 'profile.html', {'profile': user_profile})