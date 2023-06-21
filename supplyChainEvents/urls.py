from django.urls import path, include
from rest_framework import routers
from .views import (SupplyChainEventViewSet,EventTypeViewSet, EventStatusViewSet)

events_router = routers.DefaultRouter()
events_router.register(prefix='events', viewset=SupplyChainEventViewSet)

event_types_router = routers.DefaultRouter()
event_types_router.register(prefix='events/types', viewset=EventTypeViewSet)

event_status_router = routers.DefaultRouter()
event_status_router.register(prefix='event/status', viewset=EventStatusViewSet)

urlpatterns = [
    path('supplychain/', include(
        [
            path('', include(events_router.urls)),
            path('', include(event_types_router.urls)),
            path('', include(event_status_router.urls))
        ]

    )),
]

