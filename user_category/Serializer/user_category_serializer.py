from rest_framework import serializers 
from user_category.Model.user_category_model import UserCategoryModel 


from category.Serializer.category_serializer import CategorySerializer 

from User.Serializer.user_serializer import GetUserSerializer 



# a serializer for the Creation of  UserCategoryModel 


class CreateUserCategorySerializer(serializers.ModelSerializer):


    class Meta: 
        model = UserCategoryModel
        fields = ['users', 'category'] 
        read_only_fields = ['created_at', 'updated_at']



# a serializer for the Retrieval of  UserCategoryModel 


class GetUserCategorySerializer(serializers.ModelSerializer):
    users = GetUserSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta: 
        model = UserCategoryModel
        fields = ['users', 'category', 'created_at', 'updated_at'] 
        read_only_fields = ['created_at', 'updated_at']