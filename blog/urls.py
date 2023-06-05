from django.urls import path

from blog.views import (
    HomeView,
    PostDetailView,
    AddPostView,
    UpdatePostView,
    DeletePostView,
    AddCategoryView,
    AuthorPostListView,
    categories_view,
    ShowProfileDetailPageView,
    like_post,
    dislike_post,
)

app_name = "blog"

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "user/<str:username>",
        AuthorPostListView.as_view(),
        name="user-posts"
    ),
    path(
        "<int:pk>/profile/",
        ShowProfileDetailPageView.as_view(),
        name="detail-profile"
    ),
    path("post/create/", AddPostView.as_view(), name="post-create"),
    path("post/edit/<int:pk>/", UpdatePostView.as_view(), name="post-update"),
    path(
        "post/<int:pk>/remove/", DeletePostView.as_view(), name="post-delete"
    ),
    path(
        "category/create/", AddCategoryView.as_view(), name="category-create"
    ),
    path("category/<str:category>/", categories_view, name="category"),
    path("like/<int:pk>", like_post, name="like-post"),
    path("dislike/<int:pk>", dislike_post, name="dislike-post"),
]
