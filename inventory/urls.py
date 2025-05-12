from django.urls import path,include 

from rest_framework.routers import DefaultRouter 

from inventory.View.inventory_api_view import InventoryModelViewSet


router = DefaultRouter()

router.register('inventories',InventoryModelViewSet,basename = 'inventory')


urlpatterns = [
    
    path('',include(router.urls))
]
