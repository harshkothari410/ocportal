# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojp', '0003_auto_20161116_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='num_of_correct_tries',
            field=models.IntegerField(default=0),
        ),
    ]
