from rest_framework import serializers 
from order_item.Model.order_item_model import OrderItemModel 

from order.Serializer.order_serializer import GetOrderSerializer 
from product.Serializer.product_serializer import GetProductSerializer 

# serializer for creation of order item serializer 

class CreateOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItemModel
        fields = '__all__'

# Serializer for get order item serializer 


class GetOrderItemSerializer(serializers.ModelSerializer):

    order= GetOrderSerializer(read_only = True)
    product= GetProductSerializer(read_only = True)

    class Meta:
        model = OrderItemModel
        fields = '__all__'