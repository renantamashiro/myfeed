from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.views import APIView

from api.models import SiteConfig, SiteContent
from api.serializers import UserSerializer, SiteConfigSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SiteConfigList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SiteConfig.objects.all()
    serializer_class = SiteConfigSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SiteConfigDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SiteConfig.objects.all()
    serializer_class = SiteConfigSerializer

class SiteContentView(APIView):
    def run_threads():
        pass