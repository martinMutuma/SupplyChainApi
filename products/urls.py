from django.urls import path, include
from rest_framework import routers
from .views import SupplyChainItemViewSet

router = routers.DefaultRouter()
router.register(prefix='items', viewset=SupplyChainItemViewSet)

urlpatterns = [
    path('supplychain/', include(router.urls)),
]