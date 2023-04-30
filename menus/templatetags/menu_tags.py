from django import template

import logger_config
from menus.models import Menu


register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(selected_menu=None):
    children = None
    menu_name = None
    logger_config.logger.error('start draw_menu')
    menu = None
    if selected_menu:
        menu = Menu.objects.prefetch_related('menu_items').get(menu_name=selected_menu)
        logger_config.logger.error(f'menu {menu}')
        menu_name = menu.menu_name
        items = menu.menu_items.filter(parent=None)
        children = menu.menu_items.filter(parent=menu)
    else:
        menus = Menu.objects.all().prefetch_related('menu_items')
        items = []
        for menu in menus:
            menu_items = menu.menu_items.filter(parent=None)
            items.extend(menu_items)
    logger_config.logger.error('finish draw_menu')
    logger_config.logger.error('menu_name', menu_name)
    logger_config.logger.error('items', items)
    logger_config.logger.error('children', children)
    logger_config.logger.error('menu', menu)

    return {'items': items, 'children': children, 'menu_name': menu_name, 'menu': menu}
