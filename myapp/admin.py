from django.contrib import admin
from .models import Post, Like, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'created_at')
    list_display_links = ('title',)  # [,]を忘れない、次に繋げるため
    ordering = ('-created_at',)  # 降順（日付の新しい順）


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')
    list_display_links = ('post',)  # [,]を忘れない、次に繋げるため


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)  # [,]を忘れない、次に繋げるため
