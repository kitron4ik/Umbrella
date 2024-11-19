from rest_framework import serializers
from .models import RegUser
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    
    class Meta:
        model = RegUser
        fields =[ 'regname', 'email', 'role_code', 'building_code','role', 'password']
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
        print(email)
        print(password)

        if not email or not password:
            raise serializers.ValidationError("Email and password are required.")

        # Authenticate the user
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid email or password.")

        if not user.is_active:
            raise serializers.ValidationError("This account is inactive.")

        data['user'] = user
        return data
        
        
     
