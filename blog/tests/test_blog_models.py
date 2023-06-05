from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import Category, Post, Comment


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name="Programming")

    def test_category_str(self):
        category = Category.objects.get(id=1)

        self.assertEqual(str(category), f"{category.name}")

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)

        self.assertEqual(category.get_absolute_url(), "/blog/")


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = get_user_model().objects.create_user(
            username="TestUser",
            password="user12345"
        )
        cls.category = Category.objects.create(name="Programming")

        cls.post = Post.objects.create(
            author=cls.author, category=cls.category, title="About Django"
        )

    def test_post_str(self):
        post = self.post

        self.assertEqual(str(post), f"{post.title}")

    def test_get_absolute_url(self):
        post = self.post

        self.assertEqual(post.get_absolute_url(), "/blog/")


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = get_user_model().objects.create_user(
            username="TestUser",
            password="user12345"
        )
        category = Category.objects.create(name="Programming")

        post = Post.objects.create(
            author=author, category=category, title="About Django"
        )
        Comment.objects.create(
            post=post, author_name="User User", content="Comment Test"
        )

    def test_category_str(self):
        comment = Comment.objects.get(id=1)

        self.assertEqual(
            str(comment),
            f"{comment.post.title} - {comment.author_name} {comment.date_added}"
        )
