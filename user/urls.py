from django.urls import path
from django.contrib.auth import views as auth_views

from user.views import (
    UserRegisterView,
    password_success_view,
    ResetPasswordView,
    ResetPasswordDoneView,
    ResetPasswordConfirmView,
    ResetPasswordCompleteView,
    UserEditView,
    EditProfileView,
    CreateUserProfileView,
)

app_name = "user"

urlpatterns = [
    path(
        "register/",
        UserRegisterView.as_view(),
        name="register"
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="registration/logout.html"
        ),
        name="logout",
    ),
    path(
        "edit-settings/",
        UserEditView.as_view(),
        name="edit-settings"
    ),
    path(
        "<int:pk>/edit-profile/",
        EditProfileView.as_view(),
        name="edit-profile"
    ),
    path(
        "create-profile/",
        CreateUserProfileView.as_view(),
        name="create-profile"
    ),
    path(
        "password-success/",
        password_success_view,
        name="password-success"
    ),
    path(
        "reset_password/",
        ResetPasswordView.as_view(),
        name="reset_password"
    ),
    path(
        "reset_password_sent/",
        ResetPasswordDoneView.as_view(),
        name="password_reset_done"
    ),
    path(
        "reset/<uidb64>/<token>/",
        ResetPasswordConfirmView.as_view(),
        name="password_reset_confirm"
    ),
    path(
        "reset_password_complete/",
        ResetPasswordCompleteView.as_view(),
        name="password_reset_complete"
    ),
]
