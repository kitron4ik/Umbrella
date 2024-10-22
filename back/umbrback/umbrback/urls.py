# from django.contrib import admin
# from django.urls import path, include
# from django.shortcuts import redirect

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('main.urls')),
   
# ]

# urls.py
from django.urls import path
from main.views import RegisterView, LoginView
from django.shortcuts import redirect

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('', lambda request: redirect('login'), name='root'),
]
