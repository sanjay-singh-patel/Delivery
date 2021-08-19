from django.shortcuts import render
from django.http import HttpResponse
import templates


# Create your views here.
def index(request):
    return render(request, 'Distributor/Distributor.html')
