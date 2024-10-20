from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Reg
from .serializers import LoginSerializer

@api_view(['GET', 'POST'])
def login_view(request):
    print("Login view called")
    if request.method == 'GET':
    
        regs = Reg.objects.all()
        serializer = LoginSerializer(regs, many=True)  # Используем сериализатор для сериализации списка объектов return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



 


