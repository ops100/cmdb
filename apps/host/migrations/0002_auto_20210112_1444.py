# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-12 06:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='created_at',
            field=models.CharField(default=datetime.datetime(2021, 1, 12, 6, 44, 53, 176000, tzinfo=utc), max_length=20),
        ),
    ]
