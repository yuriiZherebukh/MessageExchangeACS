# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-06 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
                ('institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institute.Institute')),
            ],
        ),
    ]
