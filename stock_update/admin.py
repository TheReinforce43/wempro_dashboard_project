from django.contrib import admin

# Register your models here.
from stock_update.Model.stock_update_model import StockUpdateModel 

admin.site.register(StockUpdateModel)