# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-09 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('floor', models.IntegerField()),
                ('institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institute.Institute')),
            ],
        ),
    ]