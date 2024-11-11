from django.urls import path
from django.urls import re_path as url
from  main.views import *
from . import views
from django.shortcuts import redirect



urlpatterns = [
     path('login/', views.login_view),
     path('log/', views.log_view),

     
]
