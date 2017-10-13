# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    print "Hello, I am your first request!"
    return render(request, "new.html")