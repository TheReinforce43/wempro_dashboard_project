from rest_framework.views import APIView 

from rest_framework import status 
from rest_framework.response import Response
from django.contrib.auth import  get_user_model 

from rest_framework.generics import CreateAPIView ,ListAPIView
from rest_framework.permissions import IsAuthenticated 

User = get_user_model()

# import related serializer 

from  User.Serializer.user_serializer import (
    UserSignUpSerializer,
    UserLoginSerializer,
    UserLogoutSerializer,
    GetUserSerializer
)


# User  Sing Up  API View 



class UserSignUpAPIView(CreateAPIView):
    serializer_class = UserSignUpSerializer
    queryset = User.objects.all()


# User  Logged In API View 

class UserLoginAPIView(APIView):
    

    def post(self,request,*args,**kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data,status = status.HTTP_200_OK)
    
# User log Out API View

class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserLogoutSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data,status = status.HTTP_200_OK)