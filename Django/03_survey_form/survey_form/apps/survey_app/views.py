# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

def index(request):
    del request.session['name']
    del request.session['location']
    del request.session['language']
    del request.session['comment']
    return render(request, "survey/index.html")

def submit(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        print "completed the submit function"
    return redirect('/survey/result')

def result(request):
    print "MADE IT TO THE RESULT REDIRECT"
    return render(request, "survey/result.html")
