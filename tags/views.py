from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Tag
from blog.models import Post


class TagListView(ListView):
    model = Tag
    context_object_name = 'tag_list'
    template_name = 'tags/tag_list.html'


class TagPostListView(ListView):

    context_object_name = 'posts'
    template_name = 'tags/posts_by_tag.html'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Post.objects.filter(tag=self.tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

