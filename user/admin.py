from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import Author, Profile

admin.site.register(Author, UserAdmin)
admin.site.register(Profile)
