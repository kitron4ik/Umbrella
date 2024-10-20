from rest_framework import serializers
from .models import Reg
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reg
        fields =[ 'regname', 'email', 'role_code', 'building_code','role', 'password']
        extra_kwargs = {'password':{'write_only': True}}
    def validate_email(self, value):
        if Reg.objects.filter(email=value).exists():
            raise ValidationError("Данный эмейл уже используется")
        return value
    
    def create(self, validated_data):
        reg = Reg(**validated_data)
        reg.set_password(validated_data['password'])
        reg.save()
        return reg
        
        
        
     
