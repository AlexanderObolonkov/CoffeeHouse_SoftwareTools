from .models import Position

from django.shortcuts import render
from django.views import View


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