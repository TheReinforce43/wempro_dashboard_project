from rest_framework import serializers 
from stock_update.Model.stock_update_model import StockUpdateModel

from location.Serializer.location_serializer import LocationSerializer 
from product.Serializer.product_serializer import GetProductSerializer 
from order.Serializer.order_serializer import GetOrderSerializer


class CreateStockUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model= StockUpdateModel 
        fields= "__all__"



class GetStockUpdateSerializer(serializers.ModelSerializer):

    product = GetProductSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    order = GetOrderSerializer(read_only=True)

    class Meta:
        model= StockUpdateModel 
        fields= "__all__"