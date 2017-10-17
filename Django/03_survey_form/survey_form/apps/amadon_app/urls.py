from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^home$', views.store_home),
    url(r'^create_item$', views.create_item),
    url(r'^create_item_submit$', views.create_submit),
    url(r'^delete$', views.delete_items),
    url(r'^checkout$', views.checkout),
    url(r'^order_confirmation$', views.confirmation)

]
