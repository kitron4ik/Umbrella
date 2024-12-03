from django.db import models
from account.models import RegUser

class Appointment(models.Model):
    patient = models.ForeignKey(
        RegUser, 
        on_delete=models.CASCADE, 
        related_name='patient_appointments', 
        limit_choices_to={'role': 'patient'}
    )
    doctor = models.ForeignKey(
        RegUser, 
        on_delete=models.CASCADE, 
        related_name='doctor_appointments', 
        limit_choices_to={'role': 'doctor'}
    )
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.patient.regname} -> {self.doctor.regname} ({self.date} {self.time})"
