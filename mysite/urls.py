from django.urls import path
from .views import MainView, ContactsView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('contacts', ContactsView.as_view(), name='contacts')
]
