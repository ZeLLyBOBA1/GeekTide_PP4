from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post
import io
from PIL import Image
import base64

# Create your views here.
def save_image_to_db(image_file, post):
    image = Image.open(image_file)
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")  # Или другой формат
    post.image = buffered.getvalue()
    post.save()

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.all().order_by('-published_at')  # Получаем все посты, сортируем по дате публикации
    paginator = Paginator(posts, 5)  # Разбиваем посты на страницы, по 5 постов на страницу

    page_number = request.GET.get('page')  # Получаем номер текущей страницы из параметра GET
    page_obj = paginator.get_page(page_number)  # Получаем посты для текущей страницы

    if request.is_ajax():  # Если запрос AJAX, возвращаем только посты в формате JSON
        return render(request, 'blog/post_list_ajax.html', {'page_obj': page_obj})

    return render(request, 'blog/post_list.html', {'page_obj': page_obj})