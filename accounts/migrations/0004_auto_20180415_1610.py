# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-15 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180415_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address1',
            field=models.CharField(blank=True, max_length=100, verbose_name='Address Line 1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address2',
            field=models.CharField(blank=True, max_length=100, verbose_name='Address Line 2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=750, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD format', null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=100, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=150, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]