from django import template

import logger_config
from menus.models import Menu


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, selected_menu_name):
    request = context['request']
    logger_config.logger.error('start draw_menu')
    menu = Menu.objects.prefetch_related('menu_items').get(menu_name=selected_menu_name)
    logger_config.logger.error(f'menu {menu}')
    items = menu.menu_items.filter(parent=None)
    children = menu.menu_items.filter(parent__isnull=False)
    active_item = None

    for item in items:
        if item.is_active(request):
            active_item = item
            break
    for child in children:
        if child.is_active(request):
            active_item = child
            break

    logger_config.logger.error(f'active_item is {active_item}')
    logger_config.logger.error('finish draw_menu')
    return {'items': items, 'children': children, 'menu_name': menu, 'active_item': active_item}
