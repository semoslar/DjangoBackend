# Generated by Django 3.0.5 on 2020-05-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200501_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='shopping_list_items',
            field=models.ManyToManyField(to='core.ShoppingListItem'),
        ),
    ]
