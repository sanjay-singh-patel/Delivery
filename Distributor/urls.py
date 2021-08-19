from django.contrib import admin
from django.urls import path,include

from Distributor.views import index

urlpatterns = [
    path('Distributor/', index),
]
