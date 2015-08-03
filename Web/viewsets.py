from Web.models import *
from Web.serializers import *
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class SchedulerViewSet(viewsets.ModelViewSet):
    serializer_class = SchedulerSerializer
    queryset = Schedule.objects.all()

class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()

    def get_queryset(self):
        queryset = Position.objects.all()
        profile = self.request.query_params.get('profile', None)
        if profile is not None:
            queryset = queryset.filter(place=profile)
        return queryset


