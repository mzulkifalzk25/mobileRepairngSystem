from rest_framework import serializers
from .models import Buyer, Phone


#  create serializers for your app

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    device = serializers.StringRelatedField()

    class Meta:
        model = Phone
        fields = '__all__'
