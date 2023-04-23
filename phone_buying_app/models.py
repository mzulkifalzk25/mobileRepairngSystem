from django.db import models
from phone_repairing_app.models import Customer, Device, Repair


# create your models

class Buyer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Phone(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='phones')
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.device} ({self.buyer})"
