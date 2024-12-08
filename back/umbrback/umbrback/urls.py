from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from account import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/appoint/', include('appoint.urls')),
    path('api/medcard/', include('medcard.urls')), 
]
