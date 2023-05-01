from django import template

import logger_config
from menus.models import Menu


register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(selected_menu_name):
    logger_config.logger.error('start draw_menu')
    menu = Menu.objects.prefetch_related('menu_items').get(menu_name=selected_menu_name)
    logger_config.logger.error(f'menu {menu}')
    items = menu.menu_items.filter(parent=None)
    children = menu.menu_items.filter(parent__isnull=False)
    has_active_item = False

    for item in items:
        if item.is_active:
            has_active_item = True
            break
    for child in children:
        if child.is_active:
            has_active_item = True
            break

    logger_config.logger.error(f'has_active_item is {has_active_item}')
    logger_config.logger.error('finish draw_menu')
    return {'items': items, 'children': children, 'menu_name': menu, 'has_active_item': has_active_item}
