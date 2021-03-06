# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-09 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0003_auto_20180509_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
