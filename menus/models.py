from django.db import models


class MenuItem(models.Model):
    menu_name = models.CharField(max_length=50, blank=False)
    url = models.CharField(max_length=100, blank=False)
    named_url = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.menu_name
