from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'mysite/index.html',
        )

    def post(self, request, *args, **kwargs):
        question = request.POST['QUEST']
        print(question)
        return render(
            request,
            'mysite/index.html',
        )
