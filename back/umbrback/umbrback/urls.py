from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    
]
