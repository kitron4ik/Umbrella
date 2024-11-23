from django.urls import path
from zap.views import *
from . import views
from django.urls import path
from .views import AppointmentListCreateView, AppointmentDetailView, my_appointments

urlpatterns = [
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('my-appointments/', my_appointments, name='my-appointments'),
]