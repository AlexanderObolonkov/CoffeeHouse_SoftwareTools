# import pdb
from os import getenv
from datetime import date
from .forms import QuestionForm
from .mysite_services import refresh_json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest
from django.core.mail import send_mail, BadHeaderError


class MainView(View):
    """Class Based View главной станицы"""
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET запрос для главной страницы, возвращает http ответ с главной странией"""
        form = QuestionForm()
        return render(request, 'mysite/index.html', context={
            'form': form,
        })

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """POST запрос для главной страницы, валидирует форму и в зависимости от
        результат возвращает http ответ либо с главной странией, либо со страницей
        успеха"""
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            mail = form.cleaned_data['mail']
            name = form.cleaned_data['name']
            try:
                send_mail(
                    f'From {name} | {mail}', question, mail, [getenv('MAIN_EMAIL')]
                )
            except BadHeaderError:
                return HttpResponse('Bad header')
            refresh_json(question, mail, name)
            # pdb.set_trace()
            return render(request, 'mysite/success.html', context={
                'name': name,
                'mail': mail,
                'date': date.today().isoformat(),
            })
        return render(request, 'mysite/index.html', context={
            'form': form,
        })
