# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
import re, datetime, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

def create_error_dictionary(field_name, tag, message):
    error_dict = {
        "field_name": field_name,
        "tag": tag,
        "message": message,
    }
    return error_dict

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        # errors will be a list of dictionaries containing error messages
        # each error message will be defined as a dictionary
        # error dictionary keys = field_name, tag, error_message

        # 1. confirm required fields are full
        required_fields = [
            "username", "first_name", "last_name", "email", "password", "password_conf"
        ]
        field_labels = {
            "username": "username",
            "first_name": "first name",
            "last_name": "last name",
            "email": "email",
            "birthday": "birthday",
            "password": "password",
            "password_conf": "confirm password"
        }
        for field in required_fields:
            if len(postData[field]) < 1:
                tag = "blank"
                message = field_labels[field].capitalize() + " field cannot be empty"
                error_dict = create_error_dictionary(field, tag, message)
                errors.append(error_dict)

        # 2. confirm first_name, last_name are only alpha
        alpha_fields = [
            "first_name", "last_name"
        ]
        for field in alpha_fields:
            if not postData[field].isalpha():
                tag = "invalid"
                message = field_labels[field].capitalize() + " can only receive alphabetic characters"
                error_dict = create_error_dictionary(field, tag, message)
                errors.append(error_dict)

        # 3. confirm username is alphanumeric
        alphanumeric_fields = [
            "username"
        ]
        for field in alphanumeric_fields:
            if not postData[field].isalnum():
                tag = "invalid"
                message = field_labels[field].capitalize() + " can only receive alphabetic or numeric characters"
                error_dict = create_error_dictionary(field, tag, message)
                errors.append(error_dict)

        # 4. confirm username is unique
        try:
            User.objects.get(username=postData['username'])
            tag = "duplicate"
            message = "The username already exists; please choose another"
            error_dict = create_error_dictionary(field, tag, message)
            errors.append(error_dict)
        except:
            pass

        # 5. confirm email is valid
        email_fields = [
            "email"
        ]
        for field in email_fields:
            if not EMAIL_REGEX.match(postData[field]):
                tag = "invalid"
                message = field_labels[field].capitalize() + "is not a valid email address and must be in form: address@domain.extension"
                error_dict = create_error_dictionary(field, tag, message)
                errors.append(error_dict)

        # 6. confirm email is unique
        try:
            User.objects.get(email=postData['email'])
            tag = "duplicate"
            message = "This email is already registered; please login"
            error_dict = create_error_dictionary(field, tag, message)
            errors.append(error_dict)
        except:
            pass

        # 7. conrirm password is valid, or required length, and passwords match
        password_fields = [
            "password", "password_conf"
        ]
        min_chars = 8
        for field in password_fields:
            if not PASSWORD_REGEX.match(postData[field]):
                tag = "invalid"
                message = "Passwords must have at least one number and one uppercase letter"
                error_dict = create_error_dictionary(field, tag, message)
                errors.append(error_dict)
            if len(postData[field]) < (min_chars + 1):
                tag = "short"
                message = "Passwords must have at least " + str(min_chars) + " characters"
                error_dict = create_error_dictionary(field, tag, message)
                errors.append(error_dict)
        if not postData[password_fields[0]] == postData[password_fields[1]]:
            tag = "match"
            message = "Password fields do not match"
            error_dict = create_error_dictionary(field, tag, message)
            errors.append(error_dict)

        # 8. confirm birth date is valid (before today and greater than age range)
        date_fields = [
            "birthdate"
        ]
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        age_range = 120
        this_year = int(datetime.datetime.now().strftime("%Y"))
        if (this_year - age_range) < 1900:
            min_year = 1900
        else:
            min_year = this_year - age_range
        age_range_date = datetime.datetime(
            min_year, 1, 1).strftime("%Y-%m-%d")
        for field in date_fields:
            date_from_post = postData[field]
            print date_from_post
            print today
            if postData[field]:
                if not date_from_post < today:
                    tag = "invalid"
                    message = field_labels[field].capitalize() + " is not a past date"
                    error_dict = create_error_dictionary(field, tag, message)
                    errors.append(error_dict)
                if not date_from_post > age_range_date:
                    tag = "invalid"
                    message = field_labels[field].capitalize() + " is over " + str(age_range) + " years ago"
                    error_dict = create_error_dictionary(field, tag, message)
                    errors.append(error_dict)
        return errors

    def login_validator(self, request, postData):
        errors = []
        username = postData['username']
        str_message = "The username or password are not valid"
        if not username.isalnum():
            errors.append(str_message)
            return errors
        try:
            user_obj = User.objects.get(username=username)
            user_id = user_obj.id
            stored_hash = user_obj.password
            if bcrypt.checkpw(postData['password'].encode(), stored_hash.encode()):
                request.session['user_id'] = user_id
                return errors
            else:
                errors.append(str_message)
        except:
                errors.append(str_message)
        return errors

class User(models.Model):
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
    email = models.EmailField(max_length=100, blank=False)
    birthdate = models.DateField(blank=True)
    password = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
