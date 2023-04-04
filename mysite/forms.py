from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': '2',
            'cols': '50',
            'name': 'QUEST',
            'placeholder': "Your question"
        })
    )
    mail = forms.CharField(
        widget=forms.EmailInput(attrs={
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
