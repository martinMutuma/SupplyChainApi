from products.models import SupplyChainItem
from .models import (SupplyChainEvent, EventStatus, EventType)
from core.serializers import SupplyChainBaseSerializer
from products.serializers import SupplyChainItemSerializer
from auth.serializers import UserSerializer
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.models import User


class EventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        exclude = ['created_at', 'created_by', 'updated_at']


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        exclude = ['created_at', 'created_by', 'updated_at']


class SupplyChainItemEventSerializer(SupplyChainBaseSerializer):
    item = SupplyChainItemSerializer(required=False)
    custodian = UserSerializer(required=False)
    event_status = EventStatusSerializer(required=False)
    event_type = EventTypeSerializer(required=False)

    class Meta:
        model = SupplyChainEvent
        fields = '__all__'


class SupplyChainEventSerializer(SupplyChainBaseSerializer):
    # item = SupplyChainItemSerializer(required=False)
    # # custodian = UserSerializer(required=False)
    # event_status = EventStatusSerializer(required=False)
    # event_type = EventTypeSerializer(required=False)

    class Meta:
        model = SupplyChainEvent
        fields = '__all__'

    # def create(self, validated_data):
    #     itemData = validated_data.pop('item')
    #     itemDataObj = SupplyChainItem.objects.filter(**itemData).first()

    #     custodianData = validated_data.pop('custodian')
    #     custodianDataObj = User.objects.get(**custodianData)
    #     print(custodianDataObj)

    #     event_statusData = validated_data.pop('event_status')
    #     event_statusDataObje = EventStatus.objects.filter(
    #         **event_statusData).first()
    #     event_typeData = validated_data.pop('event_type')
    #     event_typeDataObj = EventType.objects.filter(
    #         **event_typeData).first()

    #     currentEvent = SupplyChainEvent.objects.filter(
    #         item=itemDataObj, custodian=custodianDataObj, event_status=event_statusDataObje, event_type=event_typeDataObj, **validated_data)
    #     print(currentEvent)
    #     return currentEvent
