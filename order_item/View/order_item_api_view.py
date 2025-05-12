from rest_framework.viewsets import ModelViewSet 
from order_item.Model.order_item_model import OrderItemModel 
from order_item.Serializer.order_item_serializer import (
    CreateOrderItemSerializer,
    GetOrderItemSerializer
)

from product.custom_permission import ProductObjectPermission


class OrderItemModelViewSet(ModelViewSet):
    queryset = OrderItemModel.objects.select_related('order','product')

    # this custom permission works globally , so we can also used here  
    permission_classes=[ProductObjectPermission]


    def get_serializer_class(self):
        if self.action in ['create','update','partial_update','destroy']:
            return CreateOrderItemSerializer
        return GetOrderItemSerializer
    
    def get_queryset(self):
        queryset =super().get_queryset()

        order_id = self.request.query_params.get('oder_id',None)
        product_id = self.request.query_params.get('product_id',None)

        sales_date = self.request.query_params.get('sales_date',None)

        if order_id:
            queryset = queryset.filter(order__id = order_id)

        if product_id:
            queryset: queryset.filter(product__id= product_id)

        if sales_date:
            queryset= queryset.filter(created_at = sales_date)

        queryset = queryset.order_by('-created_at')

        return queryset 