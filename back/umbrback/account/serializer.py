from rest_framework import serializers
from .models import RegUser

from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework.response import Response

class LoginSerializer(serializers.ModelSerializer):    
    class Meta:
        
        model = RegUser
        fields =['id', 'regname', 'email', 'role_code', 'building_code','role', 'password']
        extra_kwargs = {'password':{'write_only': True}}
    def validate_email(self, value):
        if RegUser.objects.filter(email=value).exists():
            raise ValidationError("Данный эмейл уже используется")
        return value
    
    def create(self, validated_data):
        reg = RegUser(**validated_data)
        reg.set_password(validated_data['password'])
        reg.save()
        return reg
    

class LogSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email', '').strip().lower()
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("Email and password are required.")

        # Authenticate the user using email and password
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid email or password.")

        # Now `user` is an authenticated user object
        if not user.is_active:
            raise serializers.ValidationError("This account is inactive.")

        # Add user data (excluding `id`) to response
        data['user'] = {
            'regname': user.regname,
            'role': user.role,
            'role_code': user.role_code,
            'building_code': user.building_code,
        }

        # Return the actual user object (for token generation)
        data['actual_user'] = user  # Store the actual user for later use
        return data



        
     
