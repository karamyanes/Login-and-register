from rest_framework import  serializers  # we import serializer from rest_framework 
from rest_framework.permissions import IsAuthenticated
from django.db import models   # we import the models that we have it from models.py
from django.contrib.auth.models import User # this models we want to serializer, and this is defult django user model
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.state import token_backend


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):# RegissterSerializer is the object we need to serializer,serializers.ModelSerializer this is built in from rest framework and we converting something to jason based on  ModelSerializer
    class Meta:
        model = User # we try to put the model we want to serialize .from django.contrib.auth.models import User
        fields = ('id', 'username', 'password', 'first_name', 'last_name','email') # we use it to return the value that we want
        extra_kwargs = {# it makes the passwords only stars no one can see it
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
                validated_data['username'],
                password = validated_data['password'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                email=validated_data['email'],
            )
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # we use '__all__' if we want to return every thing 


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):#when we login we will find username and id this is token help us to get them can do this by creating a custom serializer that inherits from TokenObtainPairSerializer, and extending the validate method to check for custom field values.
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)

        # Return username and id in the response
        data.update({'username': self.user.username})
        data.update({'id': self.user.id})
        data.update({'email': self.user.email})
        return data
