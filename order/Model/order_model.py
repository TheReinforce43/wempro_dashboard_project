from django.db import models 

from django.contrib.auth import get_user_model 

User = get_user_model()



class OrderModel(models.Model):

    user = models.OneToOneField(User,related_name='order_user',on_delete=models.CASCADE)
    order_description= models.TextField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return f"order id : {self.id} , user : {self.user.email}"