from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import FoodItem,Booking
from .serializers import FoodItemSerializer,BookingSerializer

class FoodItemCreateView(generics.CreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(donor=self.request.user)

from rest_framework import generics, permissions
from .models import FoodItem
from .serializers import FoodItemSerializer
from datetime import date

class FoodListView(generics.ListAPIView):
    serializer_class = FoodItemSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view food

    def get_queryset(self):
        return FoodItem.objects.filter(expiration_date__gte=date.today()).order_by('-posted_at')

class BookingView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class MyBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(receiver=self.request.user).order_by('-booked_at')
    
class DonorBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(food__donor=self.request.user).order_by('-booked_at')
