from django import forms
from .import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'intro', 'achievements']


class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = '__all__'


class DescriptionForm(forms.ModelForm):
    class Meta:
        model = models.Description
        fields = '__all__'

class LogoForm(forms.ModelForm):
    class Meta:
        model = models.Logo
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'


