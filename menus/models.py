from django.db import models
from django.urls import resolve


class Menu(models.Model):
    menu_name = models.CharField(max_length=50, blank=False)


class MenuItem(models.Model):
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')
    title = models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=100, blank=False)
    named_url = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.menu_name

    def is_active(self, request):
        resolved_url = resolve(request.path_info)
        return self.url == resolved_url.url_name
