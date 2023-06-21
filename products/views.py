from rest_framework import permissions
from rest_framework import viewsets
from .models import SupplyChainItem
from .serializers import SupplyChainItemSerializer

class SupplyChainItemViewSet(viewsets.ModelViewSet):
    queryset = SupplyChainItem.objects.select_related('created_by').all()
    serializer_class = SupplyChainItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def perform_create(self, serializer):
        serializer.save(created_by=self.request.user )