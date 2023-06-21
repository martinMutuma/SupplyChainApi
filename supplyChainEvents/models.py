from django.db import models
from core.models import BaseModel
from products.models import SupplyChainItem
from django.conf import settings


class EventStatus(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description =  models.TextField(blank=True)
    color = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    
class EventType(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(2)

    def __str__(self):
        return self.name
    

class SupplyChainEvent(BaseModel):
    item = models.ForeignKey(SupplyChainItem, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True, related_name='event_type')
    timestamp = models.DateTimeField()
    location = models.CharField(max_length=255)
    custodian =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='custodian')
    description = models.TextField(blank=True)
    action = models.CharField(max_length=255, blank=True)
    additional_parties_involved = models.TextField(blank=True)
    documentation = models.URLField(blank=True)
    signature = models.CharField(max_length=255, blank=True)
    event_status = models.ForeignKey(EventStatus, on_delete=models.SET_NULL, null=True, related_name='event_status')
    parent_event = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='%(app_label)s_%(class)sparent_event')
    next_event = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='%(app_label)s_%(class)snext_event')
    

