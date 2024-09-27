from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Profile, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  
    fields = ('user', 'text', 'created_at')  
    readonly_fields = ('created_at',)  

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'owner', 'created_at')  
    search_fields = ('title', 'description', 'tags')  
    list_filter = ('created_at', 'owner')  
    summernote_fields = ('description',)  

    
    inlines = [CommentInline]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'first_name', 'last_name', 'bio', 'avatar')
    search_fields = ('user__username', 'display_name', 'first_name', 'last_name', 'bio')
    list_filter = ('user',) 


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')  
    search_fields = ('user__username', 'post__title')  
    list_filter = ('post',)