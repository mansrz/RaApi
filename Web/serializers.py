from rest_framework import serializers
from Web.models import *
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        field = ('id','name','url')

class PositionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Position
        fields = ('id', 'name', 'longitude', 'latitude', 'cota', 'profile', 'bloque', 'codigo','unidad', 'tipo','planta','descripction')

