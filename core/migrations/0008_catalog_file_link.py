# Generated by Django 3.0.5 on 2020-05-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_shoppinglist_shopping_list_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='file_link',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
