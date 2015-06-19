# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden
from suds.xsd.doctor import ImportDoctor, Import
from suds.client import Client


from models import PlaceType, Position
# Create your views here.

def verifyUser(request):

    try:
        user = request.GET['user'].strip()
        pwd = request.GET['pwd'].strip()
    except:
        return HttpResponseBadRequest('Error parametros')
    from django.contrib.auth import authenticate
    auth = authenticate(username = user , password = pwd)
    if auth is not None:
       return HttpResponse(auth.pk,status=202)
    else:

        url = 'http://ws.espol.edu.ec/saac/wsandroid.asmx?WSDL'
        imp = Import('http://www.w3.org/2001/XMLSchema')
        imp.filter.add('http://tempuri.org/')
        doctor = ImportDoctor(imp)
        client = Client(url, doctor=doctor)
        auth = client.service.autenticacion(user,pwd)

        if auth == True:
            auth = User.objects.create_user(username=user, password=pwd)
            auth.save()
            auth = authenticate(username = user , password = pwd)
            return HttpResponse(auth.pk,status=202)
        else:
            return HttpResponseForbidden('Autenticacion Fallida')



def placeTypes(request):
    print request
    if request.method == 'GET':
        places = PlaceType.objects.all()
        print places
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
                type_place = PlaceType.objects.get(pk=place)
            except:
                return HttpResponseBadRequest()
            if len(name) <2:
                return HttpResponseBadRequest()
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

    if user.is_staff:
        if request.method == 'GET':
            context = {'admin':'true'}
            return render(request, template, context)
    else:
        if request.method == 'GET':
            lat = request.GET.get('lat', False)
            lng = request.GET.get('lng', False)
            context = {'lat':lat, 'lng':lng}
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
        username = request.POST['username']
        password = request.POST['password']
    except:
        return HttpResponseBadRequest('Bad parameters')

    from django.contrib.auth import authenticate, login

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)

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

       
def search(request):
    if request.method == 'GET':
        term = request.GET.get('term')
        if not term:
            return redirect('/')

        from django.db.models import Q
        from itertools import chain
        import re

        # Remove leading and trailing whitespaces
        # Make every number of whitespaces in row a single space
        term = re.sub(r'\s+', ' ', term.strip())

        # Discard spanish's articles and prepositions
        es = ['el', 'la', 'lo', 'los', 'las', 'al', 'al', 'del', 'a', 'de', 'en']
        terms = term.split(' ')
        terms = [term for term in terms if term not in es]
        term = ' '.join(terms)

        positions = Position.objects.filter(Q(name__contains=term.lower()))
        response = render_to_response(
        'positions.json',
        {'positions': positions},
        context_instance=RequestContext(request)
        )
        response['Content-Type'] = 'application/json; charset=utf-8'
        response['Cache-Control'] = 'no-cache'
        return response
  
