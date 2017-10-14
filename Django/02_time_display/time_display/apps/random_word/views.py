# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime


def index(request):
    if 'word_counter' in request.session:
        request.session['word_counter'] += 1
    else:
        request.session['word_counter'] = 1
    context = {
        "rand_string" : get_random_string(14)
    }
    return render(request, "word/index.html", context)

def reset_counter(request):
    if 'word_counter' in request.session:
        del request.session['word_counter']
    return redirect("/word")

def new_word(request):
    return redirect("/word")