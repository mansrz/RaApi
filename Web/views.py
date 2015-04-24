# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden


from models import PlaceType, Position
# Create your views here.

def placeTypes(request):
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

def positions(request):
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
        pass  
      

def map(request):
    template = 'index.html'
    if request.method == 'GET':
        context = {}
        return render(request, template, context)

def home(request):
    usuario=request.user
    template = 'login.html'
    if usuario.is_authenticated():
        return redirect('/map')
    else:
        return render(request, template, {})


@never_cache
def login(request):
    #if not request.is_ajax() or request.method != 'GET':
    #    return
    try:
        username = request.GET['username']
        password = request.GET['password']
        print password 
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
            }
            response =  HttpResponse(json.dumps(response_content))
            response['Content-Type'] = 'application/json; charset=utf-8'
            response['Cache-Control'] = 'no-cache'
            return redirect('/map')
        else:
            # Return a 'disabled account' error message
            return HttpResponseBadRequest('User have been suspended')
    else:
        # Return an 'invalid login' error message.
        return HttpResponseBadRequest('User and password are incorrect')

         
@never_cache
def logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')

       


