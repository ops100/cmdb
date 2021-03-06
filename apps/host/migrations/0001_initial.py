# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-12 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('zone', models.CharField(max_length=50)),
                ('hostname', models.CharField(max_length=50)),
                ('port', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('pkey', models.TextField(null=True)),
                ('desc', models.CharField(max_length=255, null=True)),
                ('created_at', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('-id',),
                'db_table': 'hosts',
            },
        ),
    ]
