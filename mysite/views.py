from django.shortcuts import render
from django.views import View
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from datetime import date


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mysite/index.html', )

    def post(self, request, *args, **kwargs):
        question, mail = request.POST['QUEST'], request.POST['ADDRESS']
        name = request.POST['NAME']
        errors = []
        if not question:
            errors.append('No question asked')
        if not mail:
            errors.append('No email entered')
        else:
            try:
                validate_email(mail)
            except ValidationError:
                errors.append("Wrong email format")
        if not name:
            errors.append('No name entered')

        if errors:
            return render(request, 'mysite/index.html', context={
                'errors': errors,
            })

        return render(request, 'mysite/success.html', context={
            'name': name,
            'mail': mail,
            'date': date.today().isoformat(),
        })
