from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^/login$', views.users_login),
    url(r'^/access_denied$', views.users_access_denied),
    url(r'^/logout$', views.users_logout),
    url(r'^/all$', views.users_show_all),
    url(r'^/new$', views.new_user_page),
    url(r'^/new/create$', views.create_user),
    url(r'^/(?P<id>[0-9]+)$', views.read_user),
    url(r'^/(?P<id>[0-9]+)/edit$', views.edit_user_page),
    url(r'^/(?P<id>[0-9]+)/edit/update$', views.update_user),
    url(r'^/(?P<id>[0-9]+)/destroy$', views.destroy_user),
    url(r'^', views.users_index),

]
