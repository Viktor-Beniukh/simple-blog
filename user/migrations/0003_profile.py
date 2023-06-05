# Generated by Django 4.2.1 on 2023-06-04 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_add_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="default.jpg", null=True, upload_to="profile_pics"
                    ),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                ("facebook", models.CharField(blank=True, max_length=50, null=True)),
                ("twitter", models.CharField(blank=True, max_length=50, null=True)),
                ("instagram", models.CharField(blank=True, max_length=50, null=True)),
                ("telegram", models.CharField(blank=True, max_length=50, null=True)),
                ("youtube", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
