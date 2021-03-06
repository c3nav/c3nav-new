# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapdata', '0043_auto_20171110_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapupdate',
            name='changed_geometries',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='mapupdate',
            name='processed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='mapupdate',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]
