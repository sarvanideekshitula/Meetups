# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-29 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0002_auto_20180129_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastevents',
            name='comment',
            field=models.CharField(max_length=10000),
        ),
    ]