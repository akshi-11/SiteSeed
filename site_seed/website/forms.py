from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ["title", "intro", "thumb"]
        model = models.Post

