from rest_framework.routers import DefaultRouter 
from django.urls import path , include 

from stock_update.View.stock_update_view import StockUpdateModeViewSet

router = DefaultRouter()

# Create a router and register our viewset with it.
router.register(r'stock_update', StockUpdateModeViewSet, basename='product')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]