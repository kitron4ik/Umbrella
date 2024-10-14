from django.urls import path
from django.urls import re_path as url
from  main.views import *
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success')
    
]

    
