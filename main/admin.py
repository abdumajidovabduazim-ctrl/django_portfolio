from django.contrib import admin
from .models import About, Skill, Contact

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'title', 'email']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'order']
    list_editable = ['order']  # To'g'ridan admin'da tartibni o'zgartirish

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_read']
    list_filter = ['is_read']  # O'ng tomonda filter
    readonly_fields = ['name', 'email', 'message', 'created_at']  # O'zgartirib bo'lmaydi