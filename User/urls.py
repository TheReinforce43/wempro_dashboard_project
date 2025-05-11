from django.urls import path 


from User.View.user_api_view import (
    UserSignUpAPIView,
    UserLoginAPIView,
    UserLogoutAPIView
)

urlpatterns = [
    
    path('signup/',UserSignUpAPIView.as_view(),name ='signup'),
    path('login/',UserLoginAPIView.as_view(),name ='login'),
    path('logout/',UserLogoutAPIView.as_view(),name ='logout'),
]
