# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "index.html")

def new_blog(request):
    return render(request, "new_blog.html")

def create(request):
    return render(request, "index.html")

def show_blog_num(request, blog_number):
    return render(request, "blog_number.html", {'blog_number' : blog_number})

def edit_blog_num(request, blog_number):
    return render(request, "edit_blog.html", {'blog_number' : blog_number})

def destroy(request, blog_number):
    return redirect('/blogs')
