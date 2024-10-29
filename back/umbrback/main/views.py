from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import RegUser
from .serializer import LoginSerializer
import json

@api_view(['GET', 'POST'])
def login_view(request):
    print("Login view called")
    
    if request.method == 'GET':
        regs = RegUser.objects.all()
        serializer = LoginSerializer(regs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        
        # Проверяем Content-Type
        if request.content_type != 'application/json':
            return Response({"error": "Content-Type must be application/json"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return True