# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import Dictionary

def words_show(request):
    context = {"words": Dictionary.objects.all()}
    return render(request, "words/words.html", context)

def words_add(request):
    if request.method == "POST":
        if request.POST['word'] == "":
            return redirect('/words')
        new_word = Dictionary(word="", color="")
        new_word.word = request.POST['word']
        new_word.color = request.POST['color']
        font_check_box = request.POST.get('large_font', False)
        print "HERE IS THE CHECK BOX VAL >>>>> " + str(font_check_box)
        if font_check_box:
            new_word.font_size = "large"
        else:
            new_word.font_size = "normal"
        new_word.save()
    return redirect('/words')

def words_delete(request):
    for word in Dictionary.objects.all():
        word.delete()
    return redirect('/words')
