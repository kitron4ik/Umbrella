from django.urls import path
from . import views

urlpatterns = [
    # Получение истории болезни по ID пациента
    path('medcard/conditions/<int:patient_id>/', views.get_medical_conditions, name='get_medical_conditions'),

    # Добавление нового диагноза
    path('medcard/save-condition/', views.save_medical_condition, name='save_medical_condition'),

    # Удаление диагноза
    path('medcard/conditions/<int:condition_id>/delete/', views.delete_medical_condition, name='delete_medical_condition'),
]
