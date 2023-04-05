from os import getenv
from datetime import date
from .forms import QuestionForm

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest
from django.core.mail import send_mail, BadHeaderError


class MainView(View):
    """View главной станицы"""
    def get(self, request: HttpRequest, *args, **kwargs) -> render:
        """GET запрос для главной страницы, возвращает главную страницу"""
        form = QuestionForm()
        return render(request, 'mysite/index.html', context={
            'form': form,
        })

    def post(self, request: HttpRequest, *args, **kwargs) -> render:
        """POST запрос для главной страницы, возвращает страницу Success в случае
        успеха, Index с ошибками в случае неуспеха"""
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            mail = form.cleaned_data['mail']
            name = form.cleaned_data['name']
            try:
                send_mail(f'From {name} | {mail}', question, mail, [getenv('MAIN_EMAIL')])
            except BadHeaderError:
                return HttpResponse('Bad header')
            return render(request, 'mysite/success.html', context={
                'name': name,
                'mail': mail,
                'date': date.today().isoformat(),
            })
        return render(request, 'mysite/index.html', context={
            'form': form,
        })
