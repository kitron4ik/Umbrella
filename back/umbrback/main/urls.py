from django.urls import path
from django.urls import re_path as url
from  main.views import *
from . import views
from .views import login_view
from django.shortcuts import redirect


urlpatterns = [
     path('', login_view, name='login'),
     
]
