from django.urls import path ,include 
from rest_framework.routers import DefaultRouter 

from order_item.View.order_item_api_view import OrderItemModelViewSet

router = DefaultRouter()


# Create a router and register our viewset with it.
router.register(r'order_item', OrderItemModelViewSet, basename='order_item')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]


