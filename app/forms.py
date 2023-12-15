from django import forms
from .models import BlogPost
from django.contrib.auth.models import User

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author']




class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

BlogPostFormSet = forms.modelformset_factory(
    BlogPost,
    fields=['title', 'content',   'author'],
    extra=0,
)