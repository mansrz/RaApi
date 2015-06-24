from Web.models import *
from Web.serializers import *
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()

