# medcard/models.py
from django.db import models
from account.models import RegUser  # Импортируем модель пользователя
from appoint.models import Appointment  # Импортируем модель назначений

class MedicalCondition(models.Model):
    patient = models.ForeignKey(RegUser, on_delete=models.CASCADE, related_name='conditions')  # Пациент, которому принадлежит болезнь
    condition = models.TextField()  # Описание болезни или диагноза
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='conditions', null=True, blank=True)  # Связь с назначением, если есть
    date_added = models.DateTimeField(auto_now_add=True)  # Дата добавления диагноза

    def __str__(self):
        return f"Диагноз для {self.patient.regname} от {self.date_added}"
