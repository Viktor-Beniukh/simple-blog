from django.contrib.auth import get_user_model
from django.test import TestCase

from user.models import Profile


class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(
            username="TestUser",
            password="user12345"
        )
        Profile.objects.create(user=user)

    def test_profile_str(self):
        profile = Profile.objects.get(id=1)

        self.assertEqual(str(profile), f"{profile.user}")

    def test_get_absolute_url(self):
        profile = Profile.objects.get(id=1)

        self.assertEqual(profile.get_absolute_url(), "/blog/")
