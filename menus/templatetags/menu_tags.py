from django import template

from menus.models import MenuItem


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.all()
    active_menu = menu_items.filter(menu_name=menu_name).first()

    def draw_list(menu_item):
        if menu_item == active_menu:
            return f'<li class="active"><a href="{menu_item.url}">{menu_item.menu_name}</a></li>'
        return f'<li><a href="{menu_item.url}">{menu_item.menu_name}</a></li>'

    menu_html = ''

    def get_rendered_parents(menu_item):
        if menu_item.parent is None:
            return draw_list(menu_item)
        else:
            parent = menu_items.filter(menu_name=menu_item.parent.menu_name).first()
            return get_rendered_parents(parent) + draw_list(menu_item)

    menu_html += get_rendered_parents(active_menu)
    children_active_menu = menu_items.filter(parent=active_menu).first()
    if children_active_menu:
        menu_html += draw_list(children_active_menu)
    return menu_html



