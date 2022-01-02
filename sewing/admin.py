from django.contrib import admin

from .models import Product, Image


class ImageInline(admin.TabularInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    list_display = ("name", "description",)

admin.site.register(Product, ProductAdmin)