from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'personal_cabinet/index.html', {'var': 'Главная страница'})


def add(request):
    return render(request, 'personal_cabinet/add.html', {'var': 'Это страница добавления данных'})


def view(request):
    return render(request, 'personal_cabinet/view.html', {'var': 'Это страница просмотра данных'})
