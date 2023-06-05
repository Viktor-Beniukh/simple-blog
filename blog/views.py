from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import FormMixin

from blog.forms import PostForm, UpdatePostForm, CommentForm
from blog.models import Post, Category
from user.models import Author, Profile


class HomeView(ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.select_related("author", "category")
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


def categories_view(request, category):
    category_menu = Category.objects.all()
    queryset = Post.objects.select_related("author", "category")
    category_posts = queryset.filter(
        category__name__icontains=category.replace("-", " "),
    )
    paginator = Paginator(category_posts, 3)
    page = request.GET.get("page")
    category_posts = paginator.get_page(page)
    page_obj = category_posts

    context = {
        "category_menu": category_menu,
        "category": category.replace("-", " "),
        "category_posts": category_posts,
        "page_obj": page_obj
    }

    return render(request, "blog/category.html", context=context)


class AuthorPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(Author, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_created")

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = (
            super(AuthorPostListView, self)
            .get_context_data(*args, **kwargs)
        )
        context["category_menu"] = category_menu
        return context


class ShowProfileDetailPageView(DetailView):
    model = Profile
    template_name = "blog/user_show_detail_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = (
            super(ShowProfileDetailPageView, self)
            .get_context_data(**kwargs)
        )
        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm
    template_name = "blog/post_detail.html"
    queryset = Post.objects.select_related("author", "category")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.get_object().id}
        )

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["category_menu"] = category_menu
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.user = (
            self.request.user
            if self.request.user.is_authenticated
            else None
        )
        self.object.save()
        return super().form_valid(form)


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "blog/update_post.html"
    success_url = reverse_lazy("blog:index")


class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy("blog:index")


class AddCategoryView(CreateView):
    model = Category
    template_name = "blog/add_category.html"
    fields = "__all__"


def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        if request.user in post.dislikes.all():
            post.dislikes.remove(request.user)

    return redirect("blog:post-detail", pk=post.pk)


def dislike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
        if request.user in post.likes.all():
            post.likes.remove(request.user)

    return redirect("blog:post-detail", pk=post.pk)
