# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-09 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participateduser',
            old_name='meeting_id',
            new_name='meeting',
        ),
        migrations.RenameField(
            model_name='participateduser',
            old_name='participated_user_id',
            new_name='participated_user',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='participated_user',
        ),
    ]
