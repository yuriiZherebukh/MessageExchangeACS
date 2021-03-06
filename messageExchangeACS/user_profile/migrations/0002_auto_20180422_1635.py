# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-22 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.URLField(blank=True, default='/static/src/img/avatar.png', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(blank=True, choices=[('AS', 'Assistant'), ('EN', 'Engineer'), ('DC', 'Docent'), ('PS', 'Professor'), ('LA', 'laboratorian worker'), ('AD', 'Administrator'), ('SC', 'Secretary'), ('AC', 'Accountant'), ('PR', 'Pro-rector'), ('DP', 'Head of Department'), ('RC', 'Rector'), ('DR', 'Director')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='prone_number',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
