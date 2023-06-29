from django.db import models
from django.utils import timezone
from uuid import uuid4
from django.conf import settings


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   null=True, related_name='%(app_label)s_%(class)s_created_by')

    class Meta:
        abstract = True
