# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 03:03
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ojp', '0004_problem_num_of_correct_tries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
