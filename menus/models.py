from django.db import models
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
        current_url = request.path
        logger.error(f'current_url {current_url}')
        logger.error(f'self.url {self.url}')
        logger.error(f'{self} is active {self.url == current_url}')
        return self.url == current_url

    def has_children(self):
        return self.children.exists()

    def get_first_children(self):
        сhildren = MenuItem.objects.filter(parent=self)
        logger.error(f'сhildren {сhildren}')
        return сhildren


