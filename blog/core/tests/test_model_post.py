from model_mommy import mommy
from django.test import TestCase
from django.contrib.auth.models import User
from blog.core.models import Post


class PostModel(TestCase):
    def setUp(self):
        user = mommy.make(User)
        self.post = Post.objects.create(
            author=user,
            title='A test',
            content='Just a text.'
        )

    def test_create(self):
        self.assertTrue(Post.objects.exists())

    def test_created_at(self):
        import datetime
        self.assertIsInstance(self.post.created_at, datetime.datetime)

    def test_str(self):
        self.assertEqual(self.post.title, str(self.post))