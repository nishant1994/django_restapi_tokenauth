# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
status=HTTP_200_OK)


class ListSongsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides a get method handler.
    """
    serializer_class = SongsSerializer
    def get_queryset(self):
        return Songs.objects.all()


class CreateSongsView(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
 
    def perform_create(self, serializer):
        serializer.save()
