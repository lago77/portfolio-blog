from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
        username="test1user",
        email="test1@email.com",
        password="secret1",
        )
        cls.post = Post.objects.create(
        author=cls.user,
        title="A good title",
        body="Nice body content",
        )
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "test1user")
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(str(self.post), "A good title")