from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import Author

admin.site.register(Author, UserAdmin)
