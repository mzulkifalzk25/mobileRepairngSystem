from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Device(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.customer})"


class Repair(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    issue = models.TextField()
    status_choices = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In progress'),
        ('COMPLETED', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device} ({self.status})"
