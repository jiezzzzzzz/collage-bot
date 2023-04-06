from django.contrib import admin
from .models import Theme


@admin.register(Theme)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'theme_name', 'text', 'created_at']