from rest_framework import serializers
from .models import Reg

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reg
        fields =[ 'fio', 'email', 'rolecode', 'buildcode','role', 'password']
