# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
import json
from django.contrib.auth.decorators import login_required

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
   
      

def Map(request):
    template = 'index.html'
    if request.method == 'GET':
        context = {}
        return render(request, template, context)
       
    
@never_cache
def login(request):
    #if not request.is_ajax() or request.method != 'GET':
    #    return

    try:
        username = request.GET['username']
        password = request.GET['password']
    except:
        return HttpResponseBadRequest('Bad parameters')

    from django.contrib.auth import authenticate, login

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)

            # End session when the browser is closed. Otherwise use default cookie age
            if not request.GET.get('remember-me', None):
                request.session.set_expiry(0)

            response_content = {
                'username': user.username,
                'email': user.email,
                'avatar': user.profile.avatar
            }
            response =  HttpResponse(json.dumps(response_content))
            response['Content-Type'] = 'application/json; charset=utf-8'
            response['Cache-Control'] = 'no-cache'
            return response
        else:
            # Return a 'disabled account' error message
            return HttpResponseBadRequest('User have been suspended')
    else:
        # Return an 'invalid login' error message.
        return HttpResponseBadRequest('User and password are incorrect')

         

       


