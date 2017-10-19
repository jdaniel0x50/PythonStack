# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from models import *
import bcrypt


def users_index(request):
    return render(request, 'users/index.html')


def users_login(request):
    errors = User.objects.login_validator(request, request.POST)
    print errors
    if len(errors):
        # if errors, the validator returned string:
        # "The username and/or password are not valid"
        messages.error(request, errors)
        return redirect('/users')
    else:
        # if no errors, the validator completed login
        # proceed to first page
        first_page = '/users/all'
        return redirect(first_page)


def users_access_denied(request):
    return render(request, 'users/access_denied.html')


def users_logout(request):
    del request.session['user_id']
    return redirect('/users')


def new_user_page(request):
    return render(request, 'users/users_new.html')


def create_user(request):
    # setup return and redirect routes based on the button clicked
    source_post_route = request.POST.get("route_name")
    if source_post_route == "Register":
        redirect_error_route = "/users"
        redirect_success_route = "/users/all"
    elif source_post_route == "Create":
        redirect_error_route = "/users/new"
        redirect_success_route = "/users/all"

    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            extra_tags = error['field_name']
            messages.error(request, error['message'], extra_tags=extra_tags)
        return redirect(redirect_error_route)
    else:
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        birthdate = request.POST['birthdate']
        password = request.POST['password']
        password_conf = request.POST['password_conf']
        User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            birthdate=birthdate,
            password=bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        )
        if source_post_route == "Register":
            request.session['user_id'] = User.objects.get(username=username).id
    # form = NewUserForm(request.POST)
    # if form.is_valid():
    #     print "*******Form is valid!!!"
    #     username = request.POST['username']
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     email = request.POST['email']
    #     User.objects.create(
    #         username=username, first_name=first_name, last_name=last_name, email=email)
    # else:
    #     print "$$$$$$$$$$$$$$$ERRORS!!"
    #     for field in form:
    #         for error in field.errors:
    #             print error
    #             messages.add_message(request, messages.ERROR, str(error))

        # return redirect('/users/new')
    return redirect(redirect_success_route)


def users_show_all(request):
    if 'user_id' not in request.session:
        return redirect('/users/access_denied')
    context = {
        "users": User.objects.all(),
        "user_first_name": User.objects.get(id=request.session['user_id']).first_name,
    }
    return render(request, 'users/users_all.html', context)


def read_user(request, id):
    if 'user_id' not in request.session:
        return redirect('/users/access_denied')
    context = {
        "user": User.objects.get(id=id),
        "user_first_name": User.objects.get(id=request.session['user_id']).first_name,
    }
    return render(request, 'users/users_show.html', context)


def edit_user_page(request, id):
    if 'user_id' not in request.session:
        return redirect('/users/access_denied')
    context = {
        "user": User.objects.get(id=id),
        "user_first_name": User.objects.get(id=request.session['user_id']).first_name,
    }
    return render(request, 'users/users_edit.html', context)


def update_user(request, id):
    if 'user_id' not in request.session:
        return redirect('/users/access_denied')
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            extra_tags = error['field_name']
            messages.error(request, error['message'], extra_tags=extra_tags)
        return redirect('/users/' + id + '/edit')
    else:
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        birthdate = request.POST['birthdate']
        User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            birthdate=birthdate,
        )
    return redirect('/users/all')
    # form = NewUserForm(request.POST)
    # if form.is_valid():
    #     username = request.POST['username']
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     email = request.POST['email']
    #     current_user = User.objects.get(id=id)
    #     current_user.username = username
    #     current_user.first_name = first_name
    #     current_user.last_name = last_name
    #     current_user.email = email
    #     current_user.save()
    # else:
    #     for field in form:
    #         for error in field.errors:
    #             print error
    #             messages.add_message(request, messages.ERROR, str(error))
    #     return redirect('/users/{{id}}')
    # return redirect('/users')


def destroy_user(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users/all')
