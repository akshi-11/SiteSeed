from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=300, help_text='Required')

    class Meta:
        model = User
        fields = ('first_name', 'second_name', 'email', 'password')