from django.db import models
from django.urls import resolve
from logger_config import logger


class Menu(models.Model):
    menu_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.menu_name


class MenuItem(models.Model):
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')
    title = models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=100, blank=False)
    named_url = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    def is_active(self, request):
        current_url = request.path_info
        logger.error(f'resolved_url {current_url}')
        logger.error(f'self.url {self.url}')
        return self.url == current_url
