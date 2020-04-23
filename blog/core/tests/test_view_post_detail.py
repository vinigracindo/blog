from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from model_mommy import mommy

from blog.core.models import Post


class PostDetailTest(TestCase):
    def setUp(self):
        user = mommy.make(User)
        self.post = Post.objects.create(author=user, title="1", content="1")
        self.response = self.client.get(r('post', self.post.id))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/post_detail.html')

    def test_context(self):
        self.assertIn('object', self.response.context)

    def test_html(self):
        contents = [
            self.post.title,
            self.post.author.username,
            self.post.content,
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)