from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Post

class PostModelTest(TestCase):

    # Create a sample user and post to test
    def setUp(self):
            
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testpass123'
        )
        
        self.post = Post.objects.create(
            title='Test Post 1',
            author=self.user,
            content = 'This is a test post. This content is meaningless.',
        )

    def test_post_listing(self):
            self.assertEqual(f'{self.post.title}', 'Test Post 1')
            self.assertEqual(f'{self.post.author}', self.user.username)
            self.assertEqual(
                f'{self.post.content}',
                'This is a test post. This content is meaningless.')
    #--------------------------------------------------------------------------

    # Testing the custom defined methods
    def test__str__(self):
            post = self.post
            self.assertEqual(post.__str__(), self.post.title)
            self.assertEqual(str(self.post), self.post.title)

    def test_get_absolute_url(self):
        post = self.post
        url = post.get_absolute_url()
        self.assertEqual(url, f'/blog/{self.post.slug}/')
    #--------------------------------------------------------------------------

