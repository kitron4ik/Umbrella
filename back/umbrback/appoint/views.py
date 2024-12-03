from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment
from account.models import RegUser
from appoint.models import Appointment
from .serializers import AppointmentSerializer, DoctorSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def appointment_view(request):
    """Создание новой записи на прием"""
    if request.method == 'POST':
        # Проверка на тип контента
        if request.content_type != 'application/json':
            return Response({"error": "Content-Type must be application/json"}, status=status.HTTP_400_BAD_REQUEST)

        # Получаем данные из запроса
        doctor_id = request.data.get('doctor')
        appointment_date = request.data.get('date')
        appointment_time = request.data.get('time')

        # Проверка на наличие записи на это время у данного врача
        existing_appointment = Appointment.objects.filter(
            doctor_id=doctor_id,
            date=appointment_date,
            time=appointment_time
        ).exists()

        if existing_appointment:
            return Response({"error": "На это время уже есть запись"}, status=status.HTTP_400_BAD_REQUEST)

        # Если записи нет, создаем новую
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            appointment = serializer.save()
            # После сохранения записи, она будет иметь id
            return Response({
                "message": "Запись успешно создана",
                "appointment": serializer.data  # Это должно включать поле 'id'
            }, status=status.HTTP_201_CREATED)
        
        # В случае ошибки при сериализации
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"error": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def doctor_list_view(request):
    """Получение списка докторов"""
    if request.method == 'GET':
        doctors = RegUser.objects.filter(role='doctor')
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({"error": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_patients_for_doctor(request, doctor_id):
    """Получаем список пациентов для конкретного доктора"""
    try:
        # Фильтруем записи по доктору
        appointments = Appointment.objects.filter(doctor_id=doctor_id)

        # Список пациентов для данного доктора
        patients_data = []
        for appointment in appointments:
            patients_data.append({
                'appointment_id': appointment.id,
                'patient_name': appointment.patient.regname,  # Имя пациента
                'appointment_date': appointment.date,         # Дата записи
                'appointment_time': appointment.time,         # Время записи
            })
        
        return Response(patients_data, status=status.HTTP_200_OK)

    except Appointment.DoesNotExist:
        return Response({"error": "Записи не найдены"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def remove_appointment(request, appointment_id):
    """Удаление записи пациента"""
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.delete()
        return Response({"message": "Запись успешно удалена"}, status=status.HTTP_204_NO_CONTENT)
    except Appointment.DoesNotExist:
        return Response({"error": "Запись не найдена"}, status=status.HTTP_404_NOT_FOUND)
