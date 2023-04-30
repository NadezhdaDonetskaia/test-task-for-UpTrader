from django.urls import path

from menus.views import MenuView

urlpatterns = [
    path('<str:current_url>/', MenuView.as_view()),
    ]
