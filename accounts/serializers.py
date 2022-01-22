from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fileds = ('id', 'Username', 'email', 'password')
        
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only':True}}
    
def create (self, validated_data):
    UserSerializer = User.objects.create_user(validated_data['password'], validated_data['username'], validated_data['email'])
    return User