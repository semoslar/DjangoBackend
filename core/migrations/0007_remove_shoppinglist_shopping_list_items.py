# Generated by Django 3.0.5 on 2020-05-02 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_shoppinglist_shopping_list_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppinglist',
            name='shopping_list_items',
        ),
    ]
