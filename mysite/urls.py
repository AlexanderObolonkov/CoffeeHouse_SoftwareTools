from django.urls import path

from .views import (MainView, ContactsView, SuccessView, BlogView,
                    ActiveUsersView, PostDetailView, CreatePostView)

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('contacts/success/', SuccessView.as_view(), name='success'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('active_users/', ActiveUsersView.as_view(), name='active_users'),
]
