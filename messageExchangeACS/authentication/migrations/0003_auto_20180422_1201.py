# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-22 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('institute', '0001_initial'),
        ('authentication', '0002_useraccount_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='group.Group'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='institute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institute.Institute'),
        ),
    ]