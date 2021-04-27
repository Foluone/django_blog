from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    def setUp(selfself):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )
        
        self.post = Post.objects.create(
            title='test title',
            body='test body',
            author=self.user
        )
        
    def test_string_representation(self):
        post = Post(title='test title')
        self.assertEqual(str(post)), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'test title')
        self.assertEqual(f'{self.post.author}', ''testuser)