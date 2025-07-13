from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_donor = models.BooleanField(default=False)
    is_receiver = models.BooleanField(default=False)

    def __str__(self):
        return self.username
