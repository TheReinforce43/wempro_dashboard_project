from django.urls import path,include 
from rest_framework.routers import DefaultRouter

from user_category.View.user_category_view import UserCategoryViewSet 

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'user_category', UserCategoryViewSet, basename='user_category')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]