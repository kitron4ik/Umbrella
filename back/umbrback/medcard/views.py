# views.py в приложении medcard
from rest_framework import viewsets, permissions

from .permissions import IsDoctor
from .models import MedCard
from .serializers import MedCardSerializer

class MedCardViewSet(viewsets.ModelViewSet):
    queryset = MedCard.objects.all()
    serializer_class = MedCardSerializer

    def get_permissions(self):
        """ Определяем доступ для разных ролей """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsDoctor()]
        elif self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

    def get_queryset(self):
        """ Ограничиваем видимость данных для пациентов и врачей """
        user = self.request.user
        if user.role == 'patient':
            return MedCard.objects.filter(patient=user)
        elif user.role == 'doctor':
            return MedCard.objects.filter(doctor=user)
        return MedCard.objects.none()

