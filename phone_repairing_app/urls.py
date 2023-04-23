from django.urls import path

from .views import CustomerList, CustomerDetail, DeviceList, DeviceDetail, RepairList, RepairDetail

urlpatterns = [
    path('repairs/', RepairList.as_view(), name='repair_list'),
    path('devices/', DeviceList.as_view(), name='device_list'),
    path('customers/', CustomerList.as_view(), name='customer_list'),
    path('repairs/<int:pk>/', RepairDetail.as_view(), name='repair_detail'),
    path('devices/<int:pk>/', DeviceDetail.as_view(), name='device_detail'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer_detail'),
]