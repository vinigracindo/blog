from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from model_mommy import mommy
from blog.core.models import Post


class IndexTest(TestCase):
    def setUp(self):
        user = mommy.make(User)
        self.last_10_posts = Post.objects.bulk_create([
            Post(author=user, title="1", content="1"),
            Post(author=user, title="2", content="2"),
            Post(author=user, title="3", content="3"),
            Post(author=user, title="4", content="4"),
            Post(author=user, title="5", content="5"),
            Post(author=user, title="6", content="6"),
            Post(author=user, title="7", content="7"),
            Post(author=user, title="8", content="8"),
            Post(author=user, title="9", content="9"),
            Post(author=user, title="10", content="10"),
        ])

        self.response = self.client.get(r('index'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_context(self):
        self.assertIn('page_obj', self.response.context)

    def test_html(self):
        for expected in self.last_10_posts:
            with self.subTest():
                self.assertContains(self.response, expected.title)
                self.assertContains(self.response, expected.author.username)
