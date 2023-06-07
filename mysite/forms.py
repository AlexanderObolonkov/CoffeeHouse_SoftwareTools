# mypy: ignore-errors
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import CoffeeUser, Post,Partner
from mysite.services import is_url_occupied, is_login_valid, match_mail, match_phone, check_date

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


class RegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'user123'
            }))

    email = forms.EmailField()
    image = forms.ImageField(
            required=False,
            widget=forms.FileInput(attrs={
                'class': 'form-control w-25',
                }))
    birth_date  = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(attrs={
            'placeholder': 'дд.мм.гг'
            })
        )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'placeholder': '8 (xxx) xxx-xx-xx'
            }
        )
    )

    def save(self):
        # d - сокращение от data. Нужно, чтобы было меньше писать
        d = self.cleaned_data
        print(d)
        user = CoffeeUser(name=d['name'], email=d['email'], birth_date=d['birth_date'], phone=d['phone'], image=d['image'])
        user.save()
    class Meta:
        model = CoffeeUser
        fields = ['name', 'email', 'birth_date', 'phone', 'image']


    def clean_name(self):
        """Валидация логина на длину"""
        data = self.cleaned_data['name']
        print(data)
        if not is_login_valid(data):
            self.add_error('name', 'Данный логин слишком короткий')
        return data

    def clean_email(self):
        """Валидация почты"""
        data = self.cleaned_data['email']
        if not match_mail(data):
            self.add_error('email', 'Некорректный почтовый адрес')
        return data

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if not match_phone(data):
            self.add_error('phone', "Некорректный телефонный номер")
        return data

    def clean_birth_date(self):
        data = self.cleaned_data['birth_date']
        if not check_date(data):
            self.add_error('birth_date', "Дата рождения не может быть больше, чем текущая")
        return data


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

class PartnerForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Название компании'
            }))
    email = forms.CharField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'placeholder': "Ваша почта"
        })
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'placeholder': '8 (xxx) xxx-xx-xx'
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Напишите что-нибудь о вас'
        })
    )
    def clean_name(self):
        """Валидация названия компании"""
        data = self.cleaned_data['name']
        if not is_login_valid(data):
            self.add_error('name', 'Введите имя компании')
        return data

    def clean_email(self):
        """Валидация почты"""
        data = self.cleaned_data['email']
        if not match_mail(data):
            self.add_error('email', 'Некорректный почтовый адрес')
        return data

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if not match_phone(data):
            self.add_error('phone', "Некорректный телефонный номер")
        return data
    class Meta:
        model = Partner
        fields = '__all__'