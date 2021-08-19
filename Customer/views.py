from django.shortcuts import render
from django.http import HttpResponse
import templates


# Create your views here.
def index(request):
    return render(request,'Customer/Customer.html')

def home(request):
    return render(request,'home.html')