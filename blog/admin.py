from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}  # nom yozilsa slug avtomatik

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_published', 'created_at']
    list_filter = ['is_published', 'category']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}  # sarlavha yozilsa slug avtomatik