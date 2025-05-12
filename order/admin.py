from django.contrib import admin

# Register your models here.
from order.Model.order_model import OrderModel 

admin.site.register(OrderModel)