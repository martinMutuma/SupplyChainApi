from django.db import models

from core.models import BaseModel


class SupplyChainItem(BaseModel):
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=255, null=True, blank=True)
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    batch_number = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    dimensions = models.CharField(max_length=255)
    quantity = models.IntegerField()
    status = models.CharField(max_length=255)
    parent_item = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)