from django.urls import path ,include 

from rest_framework.routers import DefaultRouter 

router =  DefaultRouter ()
from order.View.order_api_view import OrderModelViewSet

# Create a router and register our viewset with it.
router.register(r'orders', OrderModelViewSet, basename='orders')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
