# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-08 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workerplace',
            name='classroom_id',
        ),
        migrations.RemoveField(
            model_name='workerplace',
            name='worker_id',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='workers',
        ),
        migrations.DeleteModel(
            name='WorkerPlace',
        ),
    ]