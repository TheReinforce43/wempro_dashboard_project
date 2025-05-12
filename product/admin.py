from django.contrib import admin

# Register your models here.
from .Model.product_model import ProductModel


admin.site.register(ProductModel)