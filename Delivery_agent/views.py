from django.shortcuts import render
from django.http import HttpResponse
import templates


# Create your views here.
def index(request1):
    return render(request1, 'Delivery_agent/Delivery_agent.html')
