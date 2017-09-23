# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Viewer(models.Model):
    username = models.CharField(max_length=100)
    points = models.BigIntegerField()

class Command(models.Model):
    name = models.CharField(max_length=40)
    text = models.CharField(max_length=2000)