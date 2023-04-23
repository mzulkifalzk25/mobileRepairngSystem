from rest_framework import viewsets
from .models import Buyer, Phone
from .serializers import BuyerSerializer, PhoneSerializer


# Create your views here.

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
