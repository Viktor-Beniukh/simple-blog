from django import forms
from ckeditor.fields import RichTextField

from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    content = RichTextField()

    class Meta:
        model = Post
        fields = ("title", "category", "content")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
        self.fields["content"].widget = forms.Textarea(attrs={"rows": 7})

    def save(self, commit=True):
        comment = super().save(commit=False)
        if self.request and self.request.user.is_authenticated:
            comment.author_name = (
                f"{self.request.user.first_name} {self.request.user.last_name}"
            )
        if commit:
            comment.save()

        return comment


class UpdatePostForm(forms.ModelForm):
    content = RichTextField()

    class Meta:
        model = Post
        fields = ("title", "content")
