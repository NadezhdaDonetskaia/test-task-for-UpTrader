from django.views.generic import TemplateView
from django.urls import resolve

from .models import MenuItem


class MenuView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_url'] = self.request.path
        context['menus'] = MenuItem.objects.filter(parent__isnull=True)
        return context
