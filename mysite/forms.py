# mypy: ignore-errors
from django.contrib.auth.forms import UserCreationForm
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import User, Post


class FeedBackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': "Ваше имя"
        })
    )
    email = forms.CharField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': "Ваша почта"
        })
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'subject',
            'placeholder': "Тема"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control md-textarea',
            'id': 'message',
            'rows': 3,
            'placeholder': "Ваше сообщение"
        })
    )


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class PostAddForm(forms.Form):
    class Meta:
        model = Post
        fields = ('title', 'description', 'content', 'image', 'author')

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Укажите заголовок статьи'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Укажите описание статьи'
        })
    )
    content = forms.CharField(
        widget=CKEditorWidget(),
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'form-control'
        })
    )
    author = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Укажите автора статьи'
        })
    )
