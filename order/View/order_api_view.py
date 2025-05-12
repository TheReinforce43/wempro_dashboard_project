from rest_framework.viewsets import ModelViewSet 

from order.Model.order_model import OrderModel 

from order.Serializer.order_serializer import (
    CreateOrderSerializer,
    GetOrderSerializer 
)

from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from order.custom_permission import OrderObjectPermission


class OrderModelViewSet(ModelViewSet):
    queryset = OrderModel.objects.select_related('user')
    permission_classes=[OrderObjectPermission]


    def  get_serializer_class(self):
        if self.action in ['create','update','partial_update','destroy']:
            return CreateOrderSerializer
        
        return GetOrderSerializer
    
    def get_queryset(self):
        queryset =super().get_queryset()

        user_id = self.request.query_params.get('user_id',None)

        if user_id :
            queryset = queryset.filter(user__id=user_id)

        queryset = queryset.order_by('-created_at')

        return queryset 
    
    # def get_permissions(self):

    #     if self.action in ['update', 'partial_update']: 
    #         self.permission_classes = [OrderObjectPermission]
    #     elif self.action in ['create',  'destroy']:
    #         self.permission_classes = [IsAdminUser]
      
    #     else:
    #         self.permission_classes = [IsAuthenticated]

    #     return super().get_permissions()
     
    

    