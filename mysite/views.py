from os import getenv
from .models import Position
from .forms import FeedBackForm

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.core.mail import send_mail, BadHeaderError


class MainView(View):
    """View главной страницы"""

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для главной страницы"""
        positions = Position.objects.all()
        return render(
            request,
            'mysite/index.html',
            context={
                'positions': positions,
                'nav_bar': 'index'
            }
        )


class ContactsView(View):
    """View страницы контактов"""

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для станицы контактов"""
        form = FeedBackForm()
        return render(request, 'mysite/contacts.html', context={
            'nav_bar': 'contacts',
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """POST-запрос для страницы контактов"""
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            mail = getenv('MAIN_EMAIL') or ''
            try:
                send_mail(f'От {name} | {from_email} | {subject}', message, from_email, [mail])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'mysite/contacts.html', context={
            'form': form,
        })


class SuccessView(View):
    """View страницы успеха"""

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для страницы успеха"""
        return render(request, 'mysite/success.html', context={
            'title': 'Спасибо'
        })


class BlogView(View):
    """View """
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для страницы полезных статей"""
        return render(request, 'mysite/blog.html', context={
            'navbar': 'blog'
        })
