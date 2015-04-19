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
        typeplace = ''
        try:
            typeplace = request.GET['type']
        except:
            typeplace = 0
        print typeplace 
        if typeplace == 0:
            positions = Position.objects.all()
            response = render_to_response(
            'positions.json',
            {'positions': positions},
            context_instance=RequestContext(request)
            )
            response['Content-Type'] = 'application/json; charset=utf-8'
            response['Cache-Control'] = 'no-cache'
            return response
        else :
            try :
                pk = int(typeplace)
                print pk
                print typeplace
            except:
                pk = 0
            positions = Position.objects.filter(place__pk=pk)
            response = render_to_response(
            'positions.json',
            {'positions': positions},
            context_instance=RequestContext(request)
            )
            response['Content-Type'] = 'application/json; charset=utf-8'
            response['Cache-Control'] = 'no-cache'
            return response
    elif request.method == 'POST':
        typeplace = ''
        try:
            typeplace = request.POST['type']
        except:
            return HttpResponseNotFound()
        positions = Position.objects.filter(place__pk=pk)
        response = render_to_response(
        'positions.json',
        {'positions': positions},
        context_instance=RequestContext(request)
        )
        response['Content-Type'] = 'application/json; charset=utf-8'
        response['Cache-Control'] = 'no-cache'
        return response
   
      



         

       


