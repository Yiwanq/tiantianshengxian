# coding:utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url('^$', views.place_order),
    url('^handle', views.order_handle),
]