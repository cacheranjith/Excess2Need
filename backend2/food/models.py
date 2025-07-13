
# Create your models here.
from django.db import models
from django.conf import settings
from accounts.models import CustomUser

class FoodItem(models.Model):
    donor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    description = models.TextField()
    address = models.CharField(max_length=255)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.donor.username}"
    
class Booking(models.Model):
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='bookings')
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('receiver', 'food')  # Prevent duplicate bookings

    def __str__(self):
        return f"{self.receiver.username} booked {self.food.name}"

