
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators
from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('id', 'username', 'password')
        

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only = True)
    token = serializers.CharField(max_length=255, read_only = True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username = username, password = password)
        
        
        if user is None:
            raise serializers.ValidationError(
                'Incorrect email or password.'
            )
        try:
            # payload = api_settings.JWT_PAYLOAD_HANDLER('user_id': user['id'])
            validators.validate_password(password = password, user=User)
            payload = api_settings.JWT_PAYLOAD_HANDLER(user)
            token = api_settings.JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User does not exist.'
            )
        return { 
            'token': token, 
            'username': user.username, 
        }