from rest_framework import serializers 

from order.Model.order_model import OrderModel 

from User.Serializer.user_serializer import GetUserSerializer 


# serializer for creation/update/destroy  for order 

class CreateOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderModel 
        fields ='__all__'


# serializer for retrieve the order model 


class GetOrderSerializer(serializers.ModelSerializer):
    user= GetUserSerializer(read_only = True)

    class Meta:
        model = OrderModel 
        fields = '__all__'

