from django.shortcuts import render
from menus.models import Menu


def home(request):
    menus = Menu.objects.all()
    return render(request, 'home.html', {'menus': menus})


