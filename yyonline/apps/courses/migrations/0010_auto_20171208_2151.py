# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-08 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_sensor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='image',
            field=models.ImageField(default='', upload_to='sensor/%Y%m', verbose_name='曲线图'),
        ),
    ]
