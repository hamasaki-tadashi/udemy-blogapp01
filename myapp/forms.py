from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'thumbnail')

    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class SearchForm(forms.Form):
    freeword = forms.CharField(
        min_length=1, max_length=30, label='', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
