from rest_framework.viewsets import ModelViewSet 
from location.Model.location_model import LocationModel 
from location.Serializer.location_serializer import LocationSerializer 

from rest_framework.permissions import IsAuthenticated


class LocationModelViewSet(ModelViewSet):
    queryset= LocationModel.objects.all()
    serializer_class= LocationSerializer

    # permission_classes=[IsAuthenticated]

    

