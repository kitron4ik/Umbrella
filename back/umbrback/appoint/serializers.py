from rest_framework import serializers
from .models import Appointment
from account.models import RegUser

# Сериализатор врача
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegUser
        fields = ['id', 'regname', 'email']

# Сериализатор записи
class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source="doctor.regname", read_only=True)
    patient_name = serializers.CharField(source="patient.regname", read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'date', 'time', 'doctor_name', 'patient_name']
