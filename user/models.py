from PIL import Image
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    image = models.ImageField(
        default="default.jpg", upload_to="profile_pics", null=True
    )
    bio = models.TextField(null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    youtube = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None
    ):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
