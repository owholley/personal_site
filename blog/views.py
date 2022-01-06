from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from .models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    fields = [
        'title',
        'content',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'



class PostListView(ListView):
    paginate_by = 5
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'

