# Generated by Django 3.0.5 on 2020-05-03 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_catalog_file_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppinglistitem',
            old_name='company',
            new_name='company_id',
        ),
    ]
