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
        response = ''
        try:
            typeplace = request.GET['type']
        except:
            typeplace = 0
        if typeplace == 0:
            positions = Position.objects.all()
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
        try:
            user = request.user
        except:
            return HttpResponseBadRequest()
        if user.is_authenticated():
            try:
                name = request.POST['name']
                lat = request.POST['lat']
                lon = request.POST['lon']
                place = request.POST['place']
            except:
                return HttpResponseBadRequest()
            if len(name) <2:
                return HttpResponseBadRequest()
            try:
                type_place = PlaceType.objects.get(pk=place)
            except:
                return HttpResponseBadRequest
            new_position = Position(name= name,latitude=lat,longitude=lon,place=type_place)
            new_position.save()
            response_content = {'status':'ok' }
            response =  HttpResponse(json.dumps(response_content))
            response['Content-Type'] = 'application/json; charset=utf-8'
            response['Cache-Control'] = 'no-cache'
            return response




def map(request):
    user = request.user
    template = 'index.html'
    if user.is_authenticated():
        if request.method == 'GET':
            context = {'admin':'true'}
            return render(request, template, context)
    else:
        return render(request, template, {})

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
            return render(request, 'login.html', {'error':'Usuario deshabilitado' })
    else:
        # Return an 'invalid login' error message.
         return render(request, 'login.html', {'error':'Credenciales no encontradas' })

         
@never_cache
def logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')

       


