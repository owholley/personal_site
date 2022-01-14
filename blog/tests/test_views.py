from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

import pytest

from ..models import Post

pytestmark = pytest.mark.django_db


class PostViewTest(TestCase):

    # create a sample user and post to test
    def setUp(self):
            
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testpass123'
        )
        
        self.post = Post.objects.create(
            title='Test Post 1',
            author = self.user,
            content = 'This is a test post. This content is meaningless.',
        )

    # Post Create
    def test_post_create_view(self):
        # Make the client authenticate
        self.client.force_login(self.user)
        # Specify the url of the view
        url = reverse("blog:create")
        # Use the client to make the request
        response = self.client.get(url)
        # Test that the response is valid
        self.assertEqual(response.status_code, 200)

    def test_post_create_form_valid(self):
        # Authenticate the user
        self.client.force_login(self.user)
        # Submit the post create form
        form_data = {
            "title": "Test Create Post 1",
            "content": "This is test create post content.",
        }
        url = reverse("blog:create")
        response = self.client.post(url, form_data)

        # Test the results for redirect
        self.assertEqual(response.status_code, 302)
        # Get the cheese based on the name
        post = Post.objects.get(title="Test Create Post 1")

        # Test that the psot matches our form
        self.assertEqual(post.title, 'Test Create Post 1')
        self.assertEqual(post.content, "This is test create post content.")
        self.assertEqual(post.author.username, self.user.username)
    #--------------------------------------------------------------------------

    # Post Detail           
    def test_post_detail_view(self):
        response = self.client.get(self.post.get_absolute_url())
        no_response = self.client.get('/posts/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test Post 1')
        self.assertTemplateUsed(response, 'blog/post_detail.html')
    #--------------------------------------------------------------------------

    # Post List 
    def test_post_list_view(self):
        response = self.client.get(reverse('blog:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post 1')
        self.assertTemplateUsed(response, 'blog/post_list.html')
    #--------------------------------------------------------------------------
