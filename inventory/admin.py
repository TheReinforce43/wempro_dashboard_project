from django.contrib import admin

# Register your models here.
from inventory.Model.inventory_model import InventoryModel


admin.site.register(InventoryModel)