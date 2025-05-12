from django.db import models 

from category.Model.category_model import CategoryModel 



class ProductModel(models.Model): 

    product_name = models.CharField(max_length=255,db_index=True,unique=True)  
    product_description = models.TextField(null=True, blank=True) 
    product_price = models.DecimalField(max_digits=10, decimal_places=2) 
    product_image = models.ImageField(upload_to='product_images/',null=True, blank=True) 
    product_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE,null=True, related_name='category_products') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self): 
        return self.product_name
    
    class Meta:
    #    here I assume that product name and category are unique together 
       unique_together = ('product_name', 'product_category')
       ordering = ['-created_at']