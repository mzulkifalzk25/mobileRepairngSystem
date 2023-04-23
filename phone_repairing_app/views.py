from rest_framework import generics
from .models import Customer, Device, Repair
from .serializers import CustomerSerializer, DeviceSerializer, RepairSerializer

# Create your views here.

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class RepairList(generics.ListCreateAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer

class RepairDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
