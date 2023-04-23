from rest_framework import serializers
from .models import Customer, Device, Repair

# create your serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    
    class Meta:
        model = Device
        fields = '__all__'

class RepairSerializer(serializers.ModelSerializer):
    device = DeviceSerializer()

    class Meta:
        model = Repair
        fields = '__all__'
