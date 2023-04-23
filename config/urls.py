from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from phone_buying_app.views import BuyerViewSet, PhoneViewSet
# from sell_phone.views import SellerListCreateView, SellingPhoneListCreateView, SellingPhoneDetailView


router = routers.DefaultRouter()
router.register(r'buyers', BuyerViewSet)
router.register(r'phones', PhoneViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/repairing/', include('phone_repairing_app.urls')),
    path('api/buying/', include('phone_buying_app.urls')),
    path('api/selling/', include('phone_selling_app.urls')),
]
