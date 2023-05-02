from django.shortcuts import render
from menus.models import Menu


def home(request, current_path=None):
    menus = Menu.objects.all()
    current_path = request.path_info
    return render(request, 'home.html', {'menus': menus, 'current_path': current_path})


