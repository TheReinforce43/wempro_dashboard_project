from django.db import models 

from location.Model.location_model import LocationModel 
from product.Model.product_model import ProductModel 


class InventoryModel(models.Model):

    location = models.ForeignKey(LocationModel,related_name='inventory_location',on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,related_name='inventory_products',on_delete=models.CASCADE)

    last_quantity= models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    