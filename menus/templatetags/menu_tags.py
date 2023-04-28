from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from menus.models import Menu

register = template.Library()

def get_menu_items(menu_name):
    return Menu.objects.filter(menu_name=menu_name, parent__isnull=True).select_related('parent')

def build_menu_tree(menu_items, parent_id=None):
    menu_dict = {}
    for item in menu_items:
        if item.parent_id == parent_id:
            menu_dict[item.id] = {
                'title': item.title,
                'url': item.url or (reverse(item.named_url) if item.named_url else ''),
                'children': build_menu_tree(menu_items, parent_id=item.id)
            }
    return menu_dict

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = get_menu_items(menu_name)
    menu_dict = build_menu_tree(menu_items)
    current_url = context['request'].path
    return mark_safe(render_menu(menu_dict, current_url))

def render_menu(menu_dict, current_url):
    result = '<ul>'
    for item_id, item in menu_dict.items():
        is_active = current_url.startswith(item['url'])
        result += f'<li class="{"active" if is_active else ""}">'
        result += f'<a href="{item["url"]}">{item["title"]}</a>'
        if item['children']:
            result += render_menu(item['children'], current_url)
        elif 'url' not in item:
            result += render_menu(item['children'], current_url)
        result += '</li>'
    result += '</ul>'
    return result
