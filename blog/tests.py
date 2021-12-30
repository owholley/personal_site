from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostTests(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post 1',
            author = 'Owen Wholley',
            content = 'This is a test post. This content is meaningless.',
        )

    def test_post_listing(self):
        self.assertEqual(f'{self.post.title}', 'Test Post 1')
        self.assertEqual(f'{self.post.author}', 'Owen Wholley')
        self.assertEqual(f'{self.post.content}', 'This is a test post. This content is meaningless.')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post 1')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_view(self):
        response = self.client.get(self.post.get_absolute_url())
        no_response = self.client.get('/posts/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test Post 1')
        self.assertTemplateUsed(response, 'blog/post_detail.html')


