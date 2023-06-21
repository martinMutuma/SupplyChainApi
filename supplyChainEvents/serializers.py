from .models import (SupplyChainEvent, EventStatus, EventType)
from core.serializers import SupplyChainBaseSerializer

class SupplyChainEventSerializer(SupplyChainBaseSerializer):
    class Meta:
        model = SupplyChainEvent
        fields = '__all__'



class EventStatusSerializer(SupplyChainBaseSerializer):
    class Meta:
        model = EventStatus
        fields = '__all__'


class EventTypeSerializer(SupplyChainBaseSerializer):
    class Meta:
        model = EventType
        fields = '__all__'