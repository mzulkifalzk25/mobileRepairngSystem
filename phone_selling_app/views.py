from rest_framework import generics
from .models import Seller, SellingPhone
from .serializers import SellerSerializer, SellingPhoneSerializer

# Create your views here

class SellerListCreateView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellingPhoneListCreateView(generics.ListCreateAPIView):
    queryset = SellingPhone.objects.all()
    serializer_class = SellingPhoneSerializer


class SellingPhoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SellingPhone.objects.all()
    serializer_class = SellingPhoneSerializer