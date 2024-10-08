from django.urls import path
from django.urls import re_path as url
from  main.views import *
urlpatterns = [
    path ('', login.views.as_Veiw(), name = 'auth')
    
]

    
