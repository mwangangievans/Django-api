from rest_framework import serializers
from authentication.models import User

class registerSerializer(serializers.ModelSerializer):
   
   password = serializers.CharField(max_length=128,min_length=4,write_only=True)
   
   class Meta:
      model = User
      fields = ['username','email','password']

     
class loginSerializer(serializers.ModelSerializer):

   password = serializers.CharField(max_length=128,min_length=4,write_only=True)


   class Meta:
      model = User  
      fields = ['username','password','token']
      read_only_fields=['token']


class UserSerializer(serializers.ModelSerializer):

   class Meta:
      model = User  
      fields = '__all__'
