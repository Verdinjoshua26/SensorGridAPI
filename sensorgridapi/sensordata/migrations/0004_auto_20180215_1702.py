# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-15 17:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensordata', '0003_auto_20180206_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensordata',
            old_name='data1',
            new_name='data',
        ),
    ]
