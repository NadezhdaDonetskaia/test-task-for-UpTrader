from django.views.generic import TemplateView
from menus.models import MenuItem


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = MenuItem.objects.filter(parent__isnull=True)
        return context
