# import re
from django import forms


class QuestionForm(forms.Form):
    """Класс формы вопроса"""
    question = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': '2',
            'cols': '50',
            'name': 'QUEST',
            'placeholder': "Your question"
        })
    )
    mail = forms.EmailField(
        widget=forms.TextInput(attrs={
            'size': '50',
            'name': 'ADDRESS',
            'placeholder': 'Your email',
        })
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'size': '25',
            'name': 'NAME',
            'placeholder': 'Your name'
        })
    )

    def clean_question(self) -> str:
        """Метод для валидации поля question формы"""
        data = self.cleaned_data['question']
        if len(data) <= 3:
            self.add_error(
                'question',
                'Question text must be more than 3 characters.'
            )
        if data.isdigit():  # re.match(r'([+-]?\d)+', data)
            self.add_error(
                'question',
                'The text of the question should not consist of only digits.'
            )
        return data
