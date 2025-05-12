from rest_framework import serializers 
from category.Model.category_model import CategoryModel 


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the CategoryModel.
    """
    class Meta:
        model = CategoryModel
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')