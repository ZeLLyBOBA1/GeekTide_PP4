from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Profile
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import RegisterForm, ProfileForm, PostForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
def index(request):
    
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 10)  

    page_number = request.GET.get('page') or 1
    posts = paginator.get_page(page_number)

    return render(request, 'index.html', {'posts': posts})




def profile_view(request, display_name):
    profile = get_object_or_404(Profile, display_name=display_name)
    return render(request, 'profile.html', {'profile': profile})




def login_view(request):
    return render(request, 'login.html')





def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})





def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  
            display_name = form.cleaned_data.get('display_name') 
            
            
            Profile.objects.create(
                user=user,
                display_name=user.username  
            )
            
            login(request, user)  
            return redirect('index')  
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})




@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', display_name=profile.display_name)
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'edit_profile.html', {'form': form})




def load_posts(request):
    page = int(request.GET.get('page', 1))  
    posts_per_page = 20  

    all_posts = Post.objects.all().select_related('owner__profile').order_by('-created_at')
    paginator = Paginator(all_posts, posts_per_page)
    
    try:
        posts = paginator.page(page)
    except:
        return JsonResponse({'posts': [], 'has_next': False})

    post_data = []
    
    for post in posts:
        post_data.append({
            'title': post.title,
            'description': post.description,
            'image_url': post.image.url if post.image else None,
            'owner_display_name': post.owner.profile.display_name,
            'owner_avatar_url': post.owner.profile.avatar.url if post.owner.profile.avatar else None,
            'tags': post.get_tags_list(), 
        })

    return JsonResponse({
        'posts': post_data,
        'has_next': posts.has_next() 
    })





@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user 
            post.save()
            return redirect('index')  
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})