from django.urls import path ,include 

from rest_framework.routers import DefaultRouter

from category.View.category_view import CategoryViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')




# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]