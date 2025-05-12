from django.contrib import admin

# Register your models here.
from order_item.Model.order_item_model import OrderItemModel 


admin.site.register(OrderItemModel)