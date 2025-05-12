from rest_framework.viewsets import ModelViewSet 

from rest_framework.permissions import IsAuthenticated
from category.Model.category_model import CategoryModel
from category.Serializer.category_serializer import CategorySerializer



class CategoryViewSet(ModelViewSet):
    """
    ViewSet for the CategoryModel.
    """
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]



    def get_queryset(self):
        queryset = super().get_queryset()

        # Add any additional filtering or ordering logic here
        category_param = self.request.query_params.get('category')
        if category_param:
            queryset = queryset.filter(name__icontains=category_param)

        return queryset