from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from authentication.serializer import UserSerializer, loginSerializer, registerSerializer
from rest_framework import response , status
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()



# Create your views here.

class RegisterApiView(ModelViewSet):
    serializer_class = registerSerializer
    queryset = User.objects.all()

    
class loginApiView(ModelViewSet):
     serializer_class = loginSerializer
     queryset = User.objects.all()

     def create(self, request, *args, **kwarg):
          email = request.data.get('usename')
          password = request.data.get('password')

          user = authenticate(username= email ,password=password)
          
          if user:
               return response.Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
          return response.Response({"message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

                 

       