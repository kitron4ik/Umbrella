from rest_framework import serializers
from .models import MedicalCondition

class MedicalConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCondition
        fields = ['id', 'patient', 'condition', 'appointment', 'date_added']  # Указываем все необходимые поля
        read_only_fields = ['date_added']  # Дата добавления будет автоматически выставляться
