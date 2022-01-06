from django import forms
from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post, Image


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class ImageInline(admin.TabularInline):
    model = Image


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    list_display = ("title", "author", "created", "modified",)

    form = PostAdminForm

admin.site.register(Post, PostAdmin)
