from django.shortcuts import render
from rest_framework.views import APIView
from .models import Login
from serialm import loginSerializer
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.
class Login(APIView):
    def get(self, request):
        output= [
            {
                "regname": output.regname,
                "email": output.email,
                "role_code": output.role_code,
                "building_code": output.building_code,
                "role": output.role,
                "password": output.password
            } for output in Login.objects.all()
        ]
        
        return Response(output)
    def post(self, request):
        serializer = loginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

def register(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
        form = LoginForm()
    return render(request, 'register.html', {'form': form})