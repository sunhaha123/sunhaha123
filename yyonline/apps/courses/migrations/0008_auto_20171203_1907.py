# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-03 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='category',
            field=models.CharField(default='1', max_length=100, verbose_name='运动类别'),
        ),
    ]
