from rest_framework.routers import DefaultRouter 
from django.urls import path , include 

from location.View.location_api_view import LocationModelViewSet


router = DefaultRouter()

router.register('locations',LocationModelViewSet,basename='location')


urlpatterns = [
    path('',include(router.urls))
]
