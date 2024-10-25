from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('c/', views.blog1, name='blog'),
]