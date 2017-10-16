# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Dictionary(models.Model):
    word = models.CharField(max_length=50)
    color = models.CharField(max_length=8)
    font_size = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

