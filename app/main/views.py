from django.shortcuts import render


def index(request):
    data = {
        'title': 'Добро пожаловать'
    }
    return render(request, 'main/index.html', data)