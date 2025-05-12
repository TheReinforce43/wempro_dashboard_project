from rest_framework import serializers 

from inventory.Model.inventory_model import InventoryModel 

from location.Serializer.location_serializer import LocationSerializer 
from product.Serializer.product_serializer import GetProductSerializer 

# create inventory serializer 

class CreateInventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryModel
        fields = "__all__"



# Get Inventory Serializer 


class GetInventorySerializer(serializers.ModelSerializer):

    location= LocationSerializer(read_only =True)
    product = GetProductSerializer(read_only =True)

    class Meta:
        model = InventoryModel
        fields ='__all__'