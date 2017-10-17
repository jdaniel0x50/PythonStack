# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key = True)
    item = models.CharField(max_length=75)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Purchase_Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    purchase_date = models.DateField(auto_now=False, auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Purchase_Line_Item(models.Model):
    id = models.AutoField(primary_key = True)
    related_purchase_order = models.ForeignKey(Purchase_Order, related_name="purchase_lines")
    item_to_purchase = models.ForeignKey(Item, related_name="purchase_items")
    quantity_to_purchase = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

