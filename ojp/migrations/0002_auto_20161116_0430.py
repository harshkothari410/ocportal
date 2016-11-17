# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='problem_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='problem',
            name='problem_type',
            field=models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='easy', max_length=100),
        ),
    ]