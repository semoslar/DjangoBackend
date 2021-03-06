# Generated by Django 3.0.5 on 2020-05-24 15:04

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200521_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='file_link',
        ),
        migrations.AddField(
            model_name='catalog',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to=core.models.upload_catalog_to),
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to=core.models.upload_company_logo_to),
        ),
    ]
