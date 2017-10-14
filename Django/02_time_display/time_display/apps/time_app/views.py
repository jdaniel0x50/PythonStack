# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
        "date_time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "date" : strftime("%A, %d %B, %Y", gmtime()),
        "time" : strftime("%H:%M %p", gmtime())
    }
    return render(request, "time/index.html", context)