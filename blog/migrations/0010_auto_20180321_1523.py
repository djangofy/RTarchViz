# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-21 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180321_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='views_count',
            new_name='view_count',
        ),
    ]
