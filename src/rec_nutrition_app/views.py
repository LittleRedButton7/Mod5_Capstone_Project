from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, LoginSerializer
from .models import User


# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'user': serializer.data,
            'status_code': status_code,
            'message': 'Horray you are registered!'
        }

        return Response(response, status_code)

class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        status_code = status.HTTP_200_OK
        print(serializer.data)
        response = {
            'token': serializer.data['token'],
            'username': serializer.data['username'],
            # 'user_id': serializer.data['id'],
        }

        return Response(response, status_code)