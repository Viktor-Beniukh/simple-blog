from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import Author


class AuthorRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = Author
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )


class EditProfileForm(UserChangeForm):

    class Meta:
        model = Author
        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined"
        )
