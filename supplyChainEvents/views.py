from rest_framework import viewsets
from .models import (SupplyChainEvent, EventStatus, EventType)
from .serializers import (SupplyChainEventSerializer,
                          EventStatusSerializer, EventTypeSerializer, SupplyChainItemEventSerializer)
from rest_framework import permissions
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class SupplyChainEventViewSet(viewsets.ModelViewSet):
    queryset = SupplyChainEvent.objects.prefetch_related().all()
    serializer_class = SupplyChainEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# def perform_create(self, serializer):

#     serializer.save(created_by=self.request.user)


class EventStatusViewSet(viewsets.ModelViewSet):
    queryset = EventStatus.objects.all()
    serializer_class = EventStatusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SupplyChainItemEventViewSet(mixins.ListModelMixin,
                                  viewsets.GenericViewSet):
    queryset = SupplyChainEvent.objects.prefetch_related().all()
    serializer_class = SupplyChainItemEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SupplyChainItemEventSerializer(queryset, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def latest(self, *args, **kwargs):
        itemId = self.kwargs['itemId']
        queryset = self.SupplyChainEvent.objects.filter(
            item=itemId).prefetch_related().all()
        queryset = queryset.order_by("-created_at").all()
        serializer = SupplyChainItemEventSerializer(queryset, many=False)
        return Response(serializer.data)

    def get_queryset(self):
        itemId = self.kwargs['itemId']
        return SupplyChainEvent.objects.filter(item=itemId).prefetch_related().all()
