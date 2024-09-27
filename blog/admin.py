from django.contrib import admin
from .models import *


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_at')
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)