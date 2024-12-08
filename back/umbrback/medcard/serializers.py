# serializers.py в приложении medcard
from rest_framework import serializers
from .models import MedCard

class MedCardSerializer(serializers.ModelSerializer):
    patient_name = serializers.ReadOnlyField(source='patient.regname')
    doctor_name = serializers.ReadOnlyField(source='doctor.regname')

    class Meta:
        model = MedCard
        fields = ['id', 'patient', 'doctor', 'appointment', 'diagnosis', 'recommendations', 'created_at', 'updated_at', 'patient_name', 'doctor_name']
