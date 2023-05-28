from django.urls import path
from .views import MainView, ContactsView, SuccessView, ActiveUsersView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('contacts/success/', SuccessView.as_view(), name='success'),
    path('active_users/', ActiveUsersView.as_view(), name='active_users')
]
