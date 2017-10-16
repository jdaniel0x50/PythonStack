from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^show$', views.index),
    url(r'^submit$', views.submit),
    url(r'^result$', views.result)
]
