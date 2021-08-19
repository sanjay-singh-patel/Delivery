from django.contrib import admin
from django.urls import path,include

from Delivery_agent.views import index

urlpatterns = [
    path('Delivery_agent/', index),
]
