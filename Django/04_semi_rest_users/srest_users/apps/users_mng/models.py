# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "Name field cannot be empty"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Name field cannot be empty"
        if len(postData['email']) < 1:
            errors['email'] = "Email field cannot be empty"
        return errors

class User(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    username = models.CharField(
        max_length=50,
        blank=False,
        validators=[
            RegexValidator(
                regex='[_.a-zA-Z0-9]+',
                message='Username can only contain letters, numbers, underscore, and periods (no spaces)'
            ),
        ]
    )
    first_name = models.CharField(
        max_length=50,
        blank=False,
        validators=[
            RegexValidator(
                regex='[ .a-zA-Z]+',
                message='Name can only contain letters, spaces, and periods'
            ),
        ]
    )
    last_name = models.CharField(
        max_length=50,
        blank=False,
        validators=[
            RegexValidator(
                regex='[ .a-zA-Z]+',
                message='Name can only contain letters, spaces, and periods'
            ),
        ]
    )
    email = models.EmailField(
        max_length=100,
        blank=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

