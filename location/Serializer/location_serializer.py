from rest_framework import serializers 
from location.Model.location_model import LocationModel 

class LocationSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = LocationModel
        fields ="__all__"