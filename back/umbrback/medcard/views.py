from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MedicalCondition, Appointment
from .serializers import MedicalConditionSerializer

@api_view(['GET'])
def get_medical_conditions(request, patient_id):
    """
    Получить историю болезни пациента по его ID.
    """
    try:
        # Получаем все медицинские состояния для указанного пациента
        conditions = MedicalCondition.objects.filter(patient_id=patient_id)
    except MedicalCondition.DoesNotExist:
        return Response({'error': 'История болезни не найдена'}, status=status.HTTP_404_NOT_FOUND)

    # Сериализуем данные
    serializer = MedicalConditionSerializer(conditions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_medical_condition(request):
    """
    Добавить новые диагнозы пациенту.
    """
    patient_id = request.data.get('patientId')
    conditions = request.data.get('conditions')  # Получаем массив диагнозов
    appointment_id = request.data.get('appointmentId')

    if not patient_id or not conditions or not isinstance(conditions, list):
        return Response({'error': 'Необходимы patientId и conditions (список)'},
                        status=status.HTTP_400_BAD_REQUEST)

    # Проверка на наличие назначений, если они указаны
    appointment = None
    if appointment_id:
        try:
            appointment = Appointment.objects.get(id=appointment_id)
        except Appointment.DoesNotExist:
            return Response({'error': 'Назначение не найдено'}, status=status.HTTP_404_NOT_FOUND)

    # Создание новых диагнозов
    medical_conditions = []
    for condition_data in conditions:
        condition = condition_data.get('condition')
        if not condition:
            return Response({'error': 'Каждый диагноз должен содержать "condition"'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        # Создаем новый объект MedicalCondition
        medical_condition = MedicalCondition(
            patient_id=patient_id,
            condition=condition,
            appointment=appointment
        )
        medical_condition.save()
        medical_conditions.append(medical_condition)

    # Сериализуем сохраненные объекты
    serializer = MedicalConditionSerializer(medical_conditions, many=True)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_medical_condition(request, condition_id):
    """
    Удалить диагноз по его ID.
    """
    try:
        condition = MedicalCondition.objects.get(id=condition_id)
    except MedicalCondition.DoesNotExist:
        return Response({'error': 'Диагноз не найден'}, status=status.HTTP_404_NOT_FOUND)

    condition.delete()
    return Response({'message': 'Диагноз успешно удалён'}, status=status.HTTP_204_NO_CONTENT)
