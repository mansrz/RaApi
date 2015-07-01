# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model): 
    name = models.CharField(max_length=64)
    url = models.CharField(max_length= 512, null = True)   
    def __unicode__(self):
        return self.name  

class Place(models.Model):
    name = models.CharField(max_length=64)
    def __unicode__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=64)
    place = models.ForeignKey(Place, related_name = "Positions")
    latitude = models.CharField(max_length=64)
    longitude = models.CharField(max_length=64)
    cota = models.IntegerField(null = True)
    profile = models.ForeignKey(Profile, related_name = "Place")
    bloque = models.CharField(max_length=64, null = True )
    codigo = models.CharField(max_length=32,  null = True)
    unidad = models.CharField(max_length=32, null = True )
    tipo = models.CharField(max_length=32, null = True )
    planta = models.IntegerField(  null = True)
    descripction = models.CharField(max_length = 256, null = True)


