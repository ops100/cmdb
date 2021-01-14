# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime
class Host(models.Model):
    name = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    port = models.IntegerField()
    username = models.CharField(max_length=50)
    pkey = models.TextField(null=True)
    desc = models.CharField(max_length=255, null=True)

    created_at = models.CharField(max_length=20, default=timezone.now())
    # created_by = models.ForeignKey(User,on_delete=models.NOT_PROVIDED, related_name='date_joined')

    def __repr__(self):
        return '<Host %r>' % self.name

    class Meta:
        db_table = 'hosts'
        ordering = ('-id',)
