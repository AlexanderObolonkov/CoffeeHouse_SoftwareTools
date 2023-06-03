from os import getenv

from .models import Position, Post, CoffeeUser
from .forms import FeedBackForm, RegistrationForm, PostAddForm

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse


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
    """View страницы полезных статей"""

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для станицы полезных статей"""
        posts = Post.objects.all().order_by('-id')
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'mysite/blog.html', context={
            'nav_bar': 'blog',
            'page_obj': page_obj
        })


class PostDetailView(View):
    """View страницы статьи"""

    def get(self, request: HttpRequest, slug: str, *args, **kwargs) -> HttpResponse:
        """GET-запрос для страницы статьи"""
        post = get_object_or_404(Post, url=slug)
        return render(request, 'mysite/post_detail.html', context={
            'post': post
        })


class CreatePostView(View):
    """View страницы создания поста"""

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для создания поста"""
        form = PostAddForm()
        return render(request, 'mysite/create_post.html', context={
            'form': form
        })

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """POST-запрос для создания поста"""
        form = PostAddForm(request.POST, files=request.FILES)
        print(request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            url = form.cleaned_data['url']
            description = form.cleaned_data['description']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            created_at = form.cleaned_data['created_at']
            author = form.cleaned_data['author']
            post = Post(title=title, url=url, description=description,
                        content=content, image=image, created_at=created_at,
                        author=author)
            post.save()
            messages.success(request, 'Статья успешно добавлена')
            return HttpResponseRedirect(reverse('blog'))
        titles = {'title': 'Заголовок',
                  'url': 'URL-адрес',
                  'description': 'Описание',
                  'content': 'Контент',
                  'image': 'Изображения статьи',
                  'created_at': 'Дата статьи'}
        for old_title, new_title in titles.items():
            if old_title in form.errors:
                form.errors[new_title] = form.errors.pop(old_title)
        print(form.errors.items())
        return render(request, 'mysite/create_post.html', context={
            'form': form
        })


class ActiveUsersView(ListView):
    model = CoffeeUser
    template_name = "mysite/active_users.html"
    paginate_by = 5

class RegistrationView(View):
    reg_form = RegistrationForm()
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'mysite/registration.html', context={
            'nav_bar':"registration",
            'reg_form': form
        })
    def post(self, request):
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            birth_date = form.cleaned_data['birth_date']
            phone = form.cleaned_data['phone']
            image = form.cleaned_data['image']
            form.save()
            return redirect("/active_users")
        return render(request, 'mysite/registration.html', context={
            'nav_bar':"registration",
            'reg_form': form
        })
