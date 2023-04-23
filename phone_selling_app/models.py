from django.db import models
from phone_repairing_app.models import Customer, Device, Repair


# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class SellingPhone(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.device} ({self.seller})"
