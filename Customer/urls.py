from django.contrib import admin
from django.urls import path,include

from Customer.views import index,home

urlpatterns = [
    path('',home),
    path('Customer/', index),
]
