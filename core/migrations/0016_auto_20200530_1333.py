# Generated by Django 3.0.5 on 2020-05-30 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200528_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppinglist',
            old_name='is_done',
            new_name='is_deleted_offline',
        ),
    ]
