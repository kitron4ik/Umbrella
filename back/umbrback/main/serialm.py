from rest_framework import serializers
from models import login

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields =[ 'fio', 'email', 'rolecode', 'buildcode','role', 'password']
