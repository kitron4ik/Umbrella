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
    # Если запрос GET
    if request.method == 'GET':
        # Проверяем, передан ли id в параметрах запроса
        user_id = request.query_params.get('id', None)

        if user_id:
            try:
                # Ищем пользователя с данным id
                user = RegUser.objects.get(id=user_id)
                serializer = LoginSerializer(user)  # Сериализуем данные пользователя
                return Response(serializer.data, status=status.HTTP_200_OK)
            except RegUser.DoesNotExist:
                return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Если id не передан, возвращаем всех пользователей
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
    # Здесь передаем сам объект пользователя, а не словарь
    refresh = RefreshToken.for_user(user)  # user — это объект модели, а не словарь
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }


@api_view(['POST'])
def log_view(request):
    if request.method == 'POST':
        # Создаем экземпляр сериализатора с данными из запроса
        serializer = LogSerializer(data=request.data)
        
        # Проверяем, если данные валидны
        if serializer.is_valid():
            # Извлекаем данные пользователя (с id)
            user_data = serializer.validated_data['user']
            
            # Извлекаем фактического пользователя для генерации токенов
            user = serializer.validated_data['actual_user']

            # Генерируем токены для пользователя
            tokens = get_tokens_for_user(user)

            # Добавляем id в user_data
            user_data['id'] = user.id  # Добавляем id пользователя в данные

            # Возвращаем успешный ответ с токенами и данными пользователя
            return Response({
                "message": "Login successful",
                "tokens": tokens,
                "user_data": user_data  # Теперь возвращаем данные пользователя с id
            }, status=status.HTTP_200_OK)

        # Если валидация не прошла, возвращаем ошибки
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Если метод запроса не POST, возвращаем ошибку
    return Response({"error": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
