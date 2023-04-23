from rest_framework import serializers
from .models import Seller, SellingPhone


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class SellingPhoneSerializer(serializers.ModelSerializer):
    seller_name = serializers.ReadOnlyField(source='seller.name')

    class Meta:
        model = SellingPhone
        fields = '__all__'
