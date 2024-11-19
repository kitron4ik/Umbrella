from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import RegUser 
from .serializer import LoginSerializer, LogSerializer
from django.contrib.auth import authenticate
import json

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['GET', 'POST'])
def login_view(request):
    # GET для получения списка зарегистрированных пользователей
    if request.method == 'GET':
        regs = RegUser.objects.all()
        serializer = LoginSerializer(regs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST для регистрации нового пользователя
    elif request.method == 'POST':
        if request.content_type != 'application/json':
            return Response({"error": "Content-Type must be application/json"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = get_tokens_for_user(user)
            return Response({
                "user": serializer.data,
                "tokens": tokens
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"error": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# Function to generate JWT tokens for the user
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST'])
def log_view(request):
    if request.method == 'POST':
        serializer = LogSerializer(data=request.data)  # Use serializer for validation
        if serializer.is_valid():
            user = serializer.validated_data['user'] 
            print(user)
            tokens = get_tokens_for_user(user)
            return Response({
                "message": "Login successful",
                "tokens": tokens
            }, status=status.HTTP_200_OK)

        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Unsupported request method
    return Response({"error": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)