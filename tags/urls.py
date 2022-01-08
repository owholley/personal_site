from django.urls import path

from .views import TagListView, TagPostListView

app_name = "tags"

urlpatterns = [
    path('', TagListView.as_view(), name='tag_list'),
    path('<slug:slug>/', TagPostListView.as_view(), name='posts_by_tag'),
]