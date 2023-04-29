from django import template
from django.utils.html import format_html
from menus.models import MenuItem


register = template.Library()


