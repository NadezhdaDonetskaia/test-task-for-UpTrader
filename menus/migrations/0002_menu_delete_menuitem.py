# Generated by Django 4.2 on 2023-04-28 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(choices=[('main_menu', 'Main Menu'), ('footer_menu', 'Footer Menu')], default='main_menu', max_length=20)),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('named_url', models.CharField(blank=True, max_length=255)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menus.menu')),
            ],
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]