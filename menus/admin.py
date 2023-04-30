from django.contrib import admin
from menus.models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['menu_name', 'title', 'url', 'named_url', 'parent']
    list_filter = ['menu_name', 'parent']
    search_fields = ['title', 'url', 'named_url']
