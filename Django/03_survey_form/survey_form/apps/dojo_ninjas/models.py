# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Dojo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    id = models.AutoField(primary_key=True)
    dojo = models.ForeignKey(Dojo, related_name="ninjas_attending")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
