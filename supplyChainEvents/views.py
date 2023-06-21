from rest_framework import viewsets
from .models import (SupplyChainEvent, EventStatus, EventType)
from .serializers import (SupplyChainEventSerializer,EventStatusSerializer, EventTypeSerializer)
from rest_framework import permissions

class SupplyChainEventViewSet(viewsets.ModelViewSet):
    queryset = SupplyChainEvent.objects.all()
    serializer_class = SupplyChainEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class EventStatusViewSet(viewsets.ModelViewSet):
    queryset = EventStatus.objects.all()
    serializer_class = EventStatusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
