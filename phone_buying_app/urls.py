from rest_framework import routers
from .views import BuyerViewSet, PhoneViewSet

router = routers.DefaultRouter()
router.register(r'buyers', BuyerViewSet)
router.register(r'phones', PhoneViewSet)

urlpatterns = router.urls