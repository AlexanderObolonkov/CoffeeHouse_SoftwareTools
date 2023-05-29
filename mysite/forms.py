# mypy: ignore-errors
from django.contrib.auth.forms import UserCreationForm
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import User, Post
from mysite.services import is_url_occupied


class FeedBackForm(forms.Form):
    """Класс формы обратной связи"""
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
    """Класс формы добавления поста"""

    class Meta:
        """Модель, с которой связана форма"""
        model = Post
        fields = '__all__'

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Укажите заголовок статьи'
        })
    )
    url = forms.SlugField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Укажите url адрес статьи (значение должно состоять только из латинских букв, цифр, '
                           'знаков подчеркивания или дефиса.)'
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
    created_at = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите дату в формате дд.мм.гг'
        })
    )
    author = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Укажите автора статьи'
        })
    )

    def clean_url(self) -> str:
        """Валидации url на уникальность"""
        data = self.cleaned_data['url']
        if is_url_occupied(data):
            self.add_error('url', 'Данный url уже занят.')
        return data
