from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Appointment
from .appserializer import AppointmentSerializer


class AppointmentListCreateView(ListCreateAPIView):
    """
    Handles listing all appointments and creating new appointments.
    """
    serializer_class = AppointmentSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return appointments for the logged-in user
        return Appointment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the appointment
        serializer.save(user=self.request.user)


class AppointmentDetailView(RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a specific appointment.
    """
    serializer_class = AppointmentSerializer
   # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure only appointments belonging to the logged-in user are accessible
        return Appointment.objects.filter(user=self.request.user)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def my_appointments(request):
    """
    Custom view to retrieve all appointments for the logged-in user.
    """
    appointments = Appointment.objects.filter(user=request.user)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

