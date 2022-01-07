from django.contrib import admin

from .models import Product, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


class ProductAdmin(admin.ModelAdmin):

    inlines = [
        ImageInline,
    ]

    list_display = ("name", "description",)

    

admin.site.register(Product, ProductAdmin)