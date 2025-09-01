from rest_framework.viewsets import ModelViewSet 
from stock_update.Serializer.stock_update_serializer import (
    CreateStockUpdateSerializer,
    GetStockUpdateSerializer
)

from stock_update.Model.stock_update_model import StockUpdateModel 

from rest_framework.permissions import IsAuthenticated 


class StockUpdateModeViewSet(ModelViewSet):
    
    queryset= StockUpdateModel.objects.select_related(
        'product',
        'order',
        'location'
    )
    # permission_classes= [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update','destroy']:
            return CreateStockUpdateSerializer
        return GetStockUpdateSerializer