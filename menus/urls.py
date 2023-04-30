from django.urls import path

from menus.views import render_menu


urlpatterns = [
    path('<path:menu_name>/', render_menu, name='draw_menu'),
]
