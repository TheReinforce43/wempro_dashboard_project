from django.urls import path , include 

from rest_framework.routers import DefaultRouter 

router = DefaultRouter() 

from product.View.product_api_view import ProductViewSet

# Create a router and register our viewset with it.
router.register(r'product', ProductViewSet, basename='product')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]