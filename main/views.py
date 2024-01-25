from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Lorem123'
    }
    return render(request, 'main/about.html', context)
