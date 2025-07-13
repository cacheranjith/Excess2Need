from rest_framework import serializers
from .models import FoodItem,Booking

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'
        read_only_fields = ['donor', 'posted_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'receiver', 'food', 'booked_at']
        read_only_fields = ['receiver', 'booked_at']

    def create(self, validated_data):
        user = self.context['request'].user
        return Booking.objects.create(receiver=user, **validated_data)