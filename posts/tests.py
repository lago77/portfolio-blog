from django.test import TestCase


from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
        username="testuser1",
        email="test1@yahoo.com",
        password="secret1",
        )
        cls.post = Post.objects.create(
        author=cls.user,
        title="A post title",
        body="Body content",
        )
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser1")
        self.assertEqual(self.post.title, "A post title")
        self.assertEqual(self.post.body, "Body content")
        self.assertEqual(str(self.post), "A post title")