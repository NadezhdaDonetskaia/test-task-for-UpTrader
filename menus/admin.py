from django import forms
from django.contrib import admin
from .models import Menu


class MenuAdminForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['menu_name', 'title', 'url', 'named_url', 'parent']
        widgets = {
            'parent': forms.Select(attrs={'style': 'width: 100%'})
        }

class MenuAdmin(admin.ModelAdmin):
    form = MenuAdminForm

admin.site.register(Menu, MenuAdmin)
