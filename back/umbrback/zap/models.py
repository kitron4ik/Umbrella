from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()  


class Appointment(models.Model):
    # Appointment fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateField()  # The date of the appointment
    time = models.TimeField()  # The time of the appointment
    created_at = models.DateTimeField(auto_now_add=True)  # When the appointment was created
    updated_at = models.DateTimeField(auto_now=True)  # When the appointment was last updated

    # Additional optional fields
    description = models.TextField(blank=True, null=True)  # Description or purpose of the appointment
    location = models.CharField(max_length=255, blank=True, null=True)  # Location of the appointment
    is_confirmed = models.BooleanField(default=False)  # Status to indicate if the appointment is confirmed

    class Meta:
        ordering = ["date", "time"]  # Default ordering by date and time
        unique_together = ("user", "date", "time")  # Prevent duplicate appointments for the same user at the same time
        db_table = "appoint"


    def __str__(self):
        return f"Appointment for {self.user} on {self.date} at {self.time}"
