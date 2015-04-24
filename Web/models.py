# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PlaceType(models.Model): 
    name = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=64)
    latitude = models.CharField(max_length=64)
    longitude = models.CharField(max_length=64)
    place = models.ForeignKey(PlaceType, related_name = "Place")
