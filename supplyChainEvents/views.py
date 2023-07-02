from typing import Any
from rest_framework import viewsets
from .models import (SupplyChainEvent, EventStatus, EventType)
from .serializers import (SupplyChainEventSerializer,
                          EventStatusSerializer, EventTypeSerializer, SupplyChainItemEventSerializer)
from rest_framework import permissions, serializers
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class SupplyChainEventViewSet(viewsets.ModelViewSet):
    queryset = SupplyChainEvent.objects.prefetch_related().all()
    serializer_class = SupplyChainEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, pk=None):
        instance = SupplyChainEvent.objects.prefetch_related().get(
            pk=pk)
        serializer = SupplyChainItemEventSerializer(instance, many=False)
        return Response(serializer.data)

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

    # def list(self, itemId):
    #     queryset = self.get_queryset(itemId)
    #     serializer = SupplyChainItemEventSerializer(queryset, many=True)

    #     return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def latest(self, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.order_by("-created_at").first()
        serializer = SupplyChainItemEventSerializer(queryset)
        return Response(serializer.data)

    def get_queryset(self):
        itemId = int(self.request.query_params.get('itemid'))
        return SupplyChainEvent.objects.filter(item=itemId).prefetch_related().all()
