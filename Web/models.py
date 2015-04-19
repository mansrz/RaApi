# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class PlaceType(models.Model): 
    name = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=64)
    latitude = models.DecimalField(max_digits = 10, decimal_places = 5)  
    longitude = models.DecimalField(max_digits = 10, decimal_places = 5)
    place = models.ForeignKey(PlaceType, related_name = "Place")
