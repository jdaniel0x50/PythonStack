# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from models import *
from forms import *

def users_home(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'users/users_all.html', context)


def show_user(request, id):
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, 'users/users_show.html', context)


def new_user(request):
    return render(request, 'users/users_new.html')


def edit_user(request, id):
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, 'users/users_edit.html', context)


def process_new_user(request):
    form = NewUserForm(request.POST)
    if form.is_valid():
        print "*******Form is valid!!!"
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email)
    else:
        print "$$$$$$$$$$$$$$$ERRORS!!"
        for field in form:
            for error in field.errors:
                print error
                messages.add_message(request, messages.ERROR, str(error))

        return redirect('/users/new')
    return redirect('/users')
    

def process_edit_user(request, id):
    form = NewUserForm(request.POST)
    if form.is_valid():
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        current_user = User.objects.get(id=id)
        current_user.username=username
        current_user.first_name=first_name
        current_user.last_name=last_name
        current_user.email=email
        current_user.save()
    else:
        for field in form:
            for error in field.errors:
                print error
                messages.add_message(request, messages.ERROR, str(error))
        return redirect('/users/{{id}}')
    return redirect('/users')


def delete_user(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')
