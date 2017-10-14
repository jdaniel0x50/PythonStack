from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new', views.new_word),
    url(r'^reset', views.reset_counter)
]