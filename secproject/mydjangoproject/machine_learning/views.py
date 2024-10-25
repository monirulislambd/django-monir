from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine_learning(request):
    return HttpResponse("<h1>Hello I am Monirul Islam</h1>")

def deep_learning(request):
    return HttpResponse("<h1>Hello This is Deep Learning Function</h1>")
