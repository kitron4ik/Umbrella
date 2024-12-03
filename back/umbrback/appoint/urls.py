from django.urls import path
from .views import appointment_view, doctor_list_view, get_patients_for_doctor, remove_appointment

urlpatterns = [
    path('appointments/', appointment_view, name='appointment-view'),
    path('appointments/<int:doctor_id>/patients/', get_patients_for_doctor, name='get_patients_for_doctor'),
    path('appointments/<int:appointment_id>/remove/', remove_appointment, name='remove_appointment'),
    path('doctors/', doctor_list_view, name='doctor-list'),
]
