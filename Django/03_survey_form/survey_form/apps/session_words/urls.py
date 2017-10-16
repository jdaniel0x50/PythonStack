from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.words_show),
    url(r'^add', views.words_add),
    url(r'^delete', views.words_delete),
]
