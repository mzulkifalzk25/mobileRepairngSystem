from django.urls import path
from .views import SellerListCreateView, SellingPhoneListCreateView, SellingPhoneDetailView


urlpatterns = [
    path('sellers/', SellerListCreateView.as_view(), name='seller-list'),
    path('phones/', SellingPhoneListCreateView.as_view(), name='selling-phone-list'),
    path('phones/<int:pk>/', SellingPhoneDetailView.as_view(), name='selling-phone-detail'),
]
