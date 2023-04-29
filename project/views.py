from django.shortcuts import render
from django.urls import resolve
from menus.models import Menu


def menu_view(request, current_url=None):
    current_url = resolve(request.path_info).url_name
    main_menu_items = Menu.objects.filter(menu_name='main_menu')
    footer_menu_items = Menu.objects.filter(menu_name='footer_menu')
    context = {
        'main_menu_items': main_menu_items,
        'footer_menu_items': footer_menu_items,
        'current_url': current_url,
    }
    return render(request, 'base.html', context)
