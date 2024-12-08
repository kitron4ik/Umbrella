# models.py в приложении medcard
from django.db import models
from account.models import RegUser  # Импорты из приложения account
from appoint.models import Appointment  # Импорты из приложения appointments

class MedCard(models.Model):
    patient = models.ForeignKey(
        RegUser, 
        on_delete=models.CASCADE, 
        related_name='medcards', 
        limit_choices_to={'role': 'patient'}
    )
    doctor = models.ForeignKey(
        RegUser, 
        on_delete=models.CASCADE, 
        related_name='doctor_medcards', 
        limit_choices_to={'role': 'doctor'}
    )
    appointment = models.ForeignKey(
        Appointment, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='medcards'
    )
    diagnosis = models.TextField()  # Диагноз пациента
    recommendations = models.TextField(blank=True, null=True)  # Рекомендации от доктора
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания записи
    updated_at = models.DateTimeField(auto_now=True)  # Дата обновления записи

    def __str__(self):
        return f"MedCard: {self.patient.regname} - {self.doctor.regname} ({self.created_at})"
