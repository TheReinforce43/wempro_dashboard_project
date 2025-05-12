from django.db import models 

from order.Model.order_model import OrderModel 
from product.Model.product_model import ProductModel 


class OrderItemModel(models.Model):

    order= models.OneToOneField(OrderModel,related_name='order',on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,related_name='order_product',on_delete=models.CASCADE)

    price= models.FloatField(default=0.0)
    quantity = models.IntegerField(default= 0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"order_id :{self.order.id} , product : {self.product.product_name} ,price :{self.price}"


    