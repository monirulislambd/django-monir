from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def analysis1(request):
    return HttpResponse("This Data Analysis1 Section")

def analysis2(request):
    return HttpResponse("This Data Analysis2 Section")

def analysis3(request):
    return HttpResponse("This Data Analysis3 Section")
