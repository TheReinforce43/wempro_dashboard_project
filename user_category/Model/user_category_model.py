from django.db import models 

from category.Model.category_model import CategoryModel

from django.contrib.auth import get_user_model 
User = get_user_model()




class UserCategoryModel(models.Model):

    users = models.ManyToManyField(User,related_name='user_category')
    category = models.OneToOneField(CategoryModel, on_delete=models.CASCADE, related_name='category_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
