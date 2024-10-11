from django.urls import path
from django.urls import re_path as url
from  main.views import *


urlpatterns = [
    path('', logins.as_view(), name='auth'),  # Исправили вызов представления
]
