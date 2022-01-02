from django.contrib import admin

from .models import Post, Image


class ImageInline(admin.TabularInline):
    model = Image


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    list_display = ("title", "author", "created", "modified",)

admin.site.register(Post, PostAdmin)
