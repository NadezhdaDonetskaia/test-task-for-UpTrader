from django.shortcuts import render, get_object_or_404
from menus.models import Menu
from logger_config import logger


def render_menu(request, menu_name):
    menu = get_object_or_404(Menu, menu_name=menu_name)
    logger.error(menu.menu_name)
    return render(request, 'menu_render.html', {'menu': menu})
