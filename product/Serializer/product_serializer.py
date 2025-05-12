from rest_framework import serializers 

from product.Model.product_model import ProductModel 


from category.Serializer.category_serializer import CategorySerializer 


# serializer for creation of product model 


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['product_name', 'product_description', 'product_price', 'product_image', 'product_category']


# serializer for  retrieve of product model
class GetProductSerializer(serializers.ModelSerializer):
    product_category = CategorySerializer(read_only=True, many=False)

    class Meta:
        model = ProductModel
        fields = ['id', 'product_name', 'product_description', 'product_price', 'product_image', 'product_category', 'created_at', 'updated_at']
      