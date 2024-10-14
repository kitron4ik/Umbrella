from django import forms
from .models import login

class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ['regname', 'email', 'role_code', 'building_code', 'role', 'password']