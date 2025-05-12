from rest_framework.viewsets import ModelViewSet 

from rest_framework.permissions import IsAuthenticated,IsAdminUser

from inventory.Model.inventory_model import InventoryModel 
from inventory.Serializer.inventory_serializer import (
    CreateInventorySerializer,
    GetInventorySerializer
)


class InventoryModelViewSet(ModelViewSet):
    queryset = InventoryModel.objects.select_related('location','product')

    # permission_classes = [IsAuthenticated] #for simplicity  , we use base authenticaton 

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update','destroy']:
            return CreateInventorySerializer
        return GetInventorySerializer
    
    def get_queryset(self):
        queryset =super().get_queryset()

        product_id =self.request.query_params.get('product_id',None)
        location_id= self.request.query_params.get('location_id',None)

        if product_id:
            queryset = queryset.filter(product__id=product_id)

        if location_id:
            queryset = queryset.filter(location__id = location_id)

        queryset= queryset.order_by('-created_at') 

        return queryset 

        

