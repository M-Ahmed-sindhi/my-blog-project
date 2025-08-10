from django.contrib import admin
from .models import Blog
from django.utils.html import format_html

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'image_tag')  # Add custom image preview

    def image_tag(self, obj):
        if obj.picture:
            return format_html('<img src="{}" width="100" height="auto" />', obj.picture.url)
        return "No Image"
    
    image_tag.short_description = 'Image'

admin.site.register(Blog, BlogAdmin)