from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightSerializer,Booking_serializer
from django.utils import timezone

class List_view(ListAPIView):
	queryset= Flight.objects.all()
	serializer_class = FlightSerializer

class Booking_view(ListAPIView):
	queryset= Booking.objects.filter(date__gte=timezone.now())	
	serializer_class = Booking_serializer