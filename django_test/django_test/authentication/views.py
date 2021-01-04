import os
import jwt
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import generics, serializers, status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .renderers import UserJSONRenderer
from .serializers import (LoginSerializer,
                          RegistrationSerializer,
                          UserSerializer)

class RegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request, **kwargs):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        token = serializer.data['token']
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(CreateAPIView):
    """Login a registered user """
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request, **kwargs):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserUpdateAPIView(UpdateAPIView):
    """
    Updates the user profile
    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        """User profile update"""
        user_data = request.data

        serializer_data = {
            'username': user_data.get('username'),
            'email': user_data.get('email')
        }
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer_data, status=status.HTTP_200_OK)