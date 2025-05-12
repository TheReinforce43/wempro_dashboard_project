from django.db import models 

class LocationModel(models.Model):

    country = models.CharField(max_length=200,unique=True,db_index=True)
    district = models.CharField(max_length=200,unique=True)
    division = models.CharField(max_length=200,unique=True)

    local_address= models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f" country : {self.country} , division : {self.division}, address:{self.local_address}"

    class Meta:
        unique_together = ['country','district','division']


    
