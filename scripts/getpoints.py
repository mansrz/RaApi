import json
import urllib2

data = json.load(urllib2.urlopen('http://sigeoespol.cepra.cedia.org.ec:8080/geoserver/Espol3D/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Espol3D:Servicios_P1_FIEC_CENT&maxFeatures=50&outputFormat=application%2Fjson'))

class Point():
    codigo = ''
    tipo = ''
    origen = ''
    nomen = ''
    lat = ''
    lon = ''
    bloque = ''
    nombre = ''
    unidad = ''

points = []
features = data['features']
names = []
for p in features:
    for d in features['properties']:
        var =  p['properties'][''+d]


