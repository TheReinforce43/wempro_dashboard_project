from django.db import models 

from product.Model.product_model import ProductModel 
from order.Model.order_model import OrderModel 
from location.Model.location_model import LocationModel 


class StockUpdateModel(models.Model):

    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name='product_stocks')
    order = models.ForeignKey(OrderModel,on_delete=models.CASCADE,related_name='order_stocks')
    location = models.ForeignKey(LocationModel,on_delete=models.CASCADE,related_name='location_stocks')
    quantity_change = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    