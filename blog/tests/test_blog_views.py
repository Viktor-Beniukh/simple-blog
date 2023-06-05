from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog.models import Category, Post

INDEX_URL = reverse("blog:index")


class PublicIndexTests(TestCase):

    def test_retrieve_index(self):
        response = self.client.get(INDEX_URL)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "blog/index.html")


class PrivateCategoryTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user_name",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_create_category(self):
        form_data = {
            "name": "Education",
        }

        self.client.post(reverse("blog:category-create"), data=form_data)
        new_category = Category.objects.get(name=form_data["name"])

        self.assertEqual(new_category.name, form_data["name"])


class PrivatePostTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user_name",
            password="user12345",
        )
        self.client.force_login(self.user)

    def test_create_post(self):
        category = Category.objects.create(name="Programming")
        form_data = {
            "category": category.id,
            "title": "About Django"
        }

        self.client.post(reverse("blog:post-create"), data=form_data)
        new_post = Post.objects.get(title=form_data["title"])

        self.assertEqual(new_post.title, form_data["title"])
        self.assertEqual(new_post.author, self.user)
        self.assertEqual(new_post.category, category)
