# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-05 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_provider', '0026_client_multiple_response_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='session',
            field=models.CharField(blank=True, db_index=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='session',
            field=models.CharField(blank=True, db_index=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='userconsent',
            name='session',
            field=models.CharField(blank=True, db_index=True, max_length=128, null=True),
        ),
    ]