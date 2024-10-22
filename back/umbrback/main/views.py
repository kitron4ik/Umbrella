# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Reg
# from .serializers import LoginSerializer

# @api_view(['GET', 'POST'])
# def login_view(request):
#     print("Login view called")
#     if request.method == 'GET':
    
#         regs = Reg.objects.all()
#         serializer = LoginSerializer(regs, many=True)  # Используем сериализатор для сериализации списка объектов return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from django.contrib.auth.models import User

class RegisterView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Пользователь успешно зарегистрирован"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Неверные учетные данные"}, status=status.HTTP_400_BAD_REQUEST)
