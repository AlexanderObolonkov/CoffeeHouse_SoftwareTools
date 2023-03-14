from django.shortcuts import render
from django.views import View
from .models import Position


class MainView(View):
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
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'mysite/contacts.html',
            context={
                'nav-bar': 'contacts'
            }
        )
