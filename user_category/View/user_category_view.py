from rest_framework.viewsets import ModelViewSet 

from rest_framework.permissions import IsAuthenticated ,IsAdminUser 
from user_category.Model.user_category_model import UserCategoryModel

from user_category.Serializer.user_category_serializer import (
     CreateUserCategorySerializer, 
     GetUserCategorySerializer
)

class UserCategoryViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user category instances.
    """
    queryset = UserCategoryModel.objects.select_related('category').prefetch_related('users')
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateUserCategorySerializer
        return GetUserCategorySerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned user category to a given user,
        by filtering against a `user` query parameter in the URL.
        """
        queryset = self.queryset
        user_id = self.request.query_params.get('user_id')
        category_id = self.request.query_params.get('category_id') 
        if user_id :
            print("user_id",user_id)
            queryset = queryset.filter(users__id=user_id)

        if category_id:
            print("category id ",category_id)   
            queryset = queryset.filter(category__id=category_id)
        return queryset
    


    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']: 
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
   