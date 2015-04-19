# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
import json

from models import PlaceType, Position
# Create your views here.

def PlaceTypes(request):
    if request.method == 'GET':
        places = PlaceType.objects.all()
        response = render_to_response(
        'places.json',
        {'places': places},
        context_instance=RequestContext(request)
        )
        response['Content-Type'] = 'application/json; charset=utf-8'
        response['Cache-Control'] = 'no-cache'
        return response

def Positions(request):
    if request.method == 'GET':
        positions = Position.objects.all()
        response = render_to_response(
        'positions.json',
        {'positions': positions},
        context_instance=RequestContext(request)
        )
        response['Content-Type'] = 'application/json; charset=utf-8'
        response['Cache-Control'] = 'no-cache'
        return response

    elif request.method == 'POST': 
        pass 
        

     


