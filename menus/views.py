from django.shortcuts import render
from menus.models import MenuItem


def menu_view(request):
    root_items = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'menu.html', {'root_items': root_items})
