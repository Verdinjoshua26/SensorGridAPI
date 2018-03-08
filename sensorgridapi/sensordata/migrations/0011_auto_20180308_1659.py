# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-08 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensordata', '0010_auto_20180301_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='battery',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='data',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='version',
            field=models.IntegerField(null=True),
        ),
    ]