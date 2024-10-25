from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def about(request):
    xy = {'x':3}
    return render(request, "about_us.html", context=xy)
