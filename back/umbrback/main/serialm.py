from rest_framework import serializers
from .models import Login

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields =[ 'regname', 'email', 'role_code', 'building_code','role', 'password']
