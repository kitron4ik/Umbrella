from django.shortcuts import render
from rest_framework.views import APIView
from models import login
from serialm import loginSerializer
from rest_framework.response import Response

# Create your views here.
class login(APIView):
    def get(self, request):
        output= [
            {
                "fio": output.fio,
                "email": output.email,
                "rolecode": output.rolecode,
                "buildcode": output.buildcode,
                "role": output.role,
                "password": output.password
            } for output in login.objects.all()
        ]
        return Response(output)
    def post(self, request):
        serializer = loginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)