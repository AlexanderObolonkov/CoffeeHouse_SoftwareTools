from os import getenv  # Кирилл
from .models import Position  # Александр
from .forms import FeedBackForm  # Кирилл

from django.shortcuts import render  # Александр
from django.views import View  # Александр
from django.http import HttpResponse, HttpResponseRedirect  # Кирилл
from django.core.mail import send_mail, BadHeaderError  # Кирилл


class MainView(View):
    """Александр"""
    def get(self, request, *args, **kwargs):
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
    """Кирилл"""
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'mysite/contacts.html', context={
            'nav_bar': 'contacts',
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'От {name} | {from_email} | {subject}', message, from_email, [getenv('MAIN_EMAIL')])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'mysite/contacts.html', context={
            'form': form,
        })


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mysite/success.html', context={
            'title': 'Спасибо'
        })
