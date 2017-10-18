from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.users_home),
    url(r'^/(?P<id>[0-9]+)$', views.show_user),
    url(r'^/new$', views.new_user),
    url(r'^/(?P<id>[0-9]+)/edit$', views.edit_user),
    url(r'^/new/process$', views.process_new_user),
    url(r'^/(?P<id>[0-9]+)/edit/process$', views.process_edit_user),
    url(r'^/(?P<id>[0-9]+)/delete$', views.delete_user),

]
