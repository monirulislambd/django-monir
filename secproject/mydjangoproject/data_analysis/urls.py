from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('ana1/',views.analysis1),
    path('ana2/',views.analysis2),
    path('ana3/',views.analysis3),

]