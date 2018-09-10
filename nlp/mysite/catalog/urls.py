#from sys import path

from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.shortcuts import render

from . import views

urlpatterns=[
    url(r'^',views.index),
    #url(r'^$',lambda request:render(request,'xyz1.html')),     #127.0.0.1/catalog/
]