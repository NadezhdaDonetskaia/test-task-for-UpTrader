from django.db import models

class Menu(models.Model):
    MENU_CHOICES = [
        ('main_menu', 'Main Menu'),
        ('footer_menu', 'Footer Menu'),
    ]
    menu_name = models.CharField(max_length=20, choices=MENU_CHOICES, default='main_menu')
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    named_url = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.title