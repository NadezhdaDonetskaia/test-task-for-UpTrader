from django import template
from django.urls import reverse
from django.db.models import Prefetch

from menus.models import MenuItem


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']

    menu_items = MenuItem.objects.select_related('parent').prefetch_related(
        Prefetch('children', queryset=MenuItem.objects.select_related('parent'))
    ).filter(menu_name=menu_name).order_by('parent_id', 'pk')

    return _draw_menu(menu_items, request)


def _draw_menu(menu_items, request):
    menu_html = '<ul>'

    for item in menu_items:
        is_active = item.is_active(request)
        has_children = item.children.exists()

        if is_active:
            menu_html += f'<li class="active">'
        else:
            menu_html += '<li>'

        if has_children:
            menu_html += f'<a href="{item.url}" class="dropdown-toggle" data-toggle="dropdown">{item.menu_name}<span class="caret"></span></a>'
            menu_html += _draw_menu(item.children.all(), request)
        else:
            url = item.url
            menu_html += f'<a href="{url}">{item.menu_name}</a>'

        menu_html += '</li>'

    menu_html += '</ul>'
    return menu_html
