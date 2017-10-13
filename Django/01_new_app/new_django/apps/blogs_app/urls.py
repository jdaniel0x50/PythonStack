from django.conf.urls import url, include
from django.contrib import admin
from . import views

print "i am here in blogs"
urlpatterns = [
    url(r'^$', views.index),
    url(r'new$', views.new_blog),
    url(r'create$', views.create),
    url(r'(?P<blog_number>[0-9]{2}$)', views.show_blog_num),
    url(r'(?P<blog_number>[0-9]{2})/edit$', views.edit_blog_num),
    url(r'(?P<blog_number>[0-9]{2})/delete$', views.destroy)
]
