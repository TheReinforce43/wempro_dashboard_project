from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated,IsAdminUser 


from product.Model.product_model import ProductModel
from product.Serializer.product_serializer import (
    CreateProductSerializer, 
    GetProductSerializer
)

from product.custom_permission import ProductObjectPermission

class ProductViewSet(ModelViewSet):
    queryset = ProductModel.objects.select_related('product_category')
    
   
    lookup_field = 'id'
    
    def get_serializer_class(self):
        if self.action in [ 'list', 'retrieve']:
            return GetProductSerializer
        return CreateProductSerializer
    
    def get_permissions(self):

        if self.action in ['update', 'partial_update']: 
            self.permission_classes = [ProductObjectPermission]
        if self.action in ['create',  'destroy']:
            self.permission_classes = [IsAdminUser]
      
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
    

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by category if provided
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = queryset.filter(product_category__id=category_id)

        # Filter by name if provided
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(product_name__icontains=name)

        queryset = queryset.order_by('-created_at')
        return queryset