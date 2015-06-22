import json
import urllib2

urls = ['http://sigeoespol.cepra.cedia.org.ec:8080/geoserver/Espol3D/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Espol3D:Servicios_P1_FIEC_CENT&maxFeatures=50&outputFormat=application%2Fjson','http://sigeoespol.cepra.cedia.org.ec:8080/geoserver/Espol3D/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Espol3D:Oficinas_P1_FIEC_CENT&maxFeatures=50&outputFormat=application%2Fjson','http://sigeoespol.cepra.cedia.org.ec:8080/geoserver/Espol3D/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Espol3D:Laboratorio_P1_FIEC_CENT&maxFeatures=50&outputFormat=application%2Fjson','http://sigeoespol.cepra.cedia.org.ec:8080/geoserver/Espol3D/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Espol3D:Infraestructura_de_Equipos_P1_FIEC_CENT&maxFeatures=50&outputFormat=application%2Fjson','http://sigeoespol.cepra.cedia.org.ec:8080/geoserver/Espol3D/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Espol3D:Bloques_FIEC_CENT&maxFeatures=50&outputFormat=application%2Fjson','http://sigeoespol.cepra.cedia.org.ec:8080/geoserver/Espol3D/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Espol3D:Aulas_P1_FIEC_CENT&maxFeatures=50&outputFormat=application%2Fjson']
for url in urls:
    data = json.load(urllib2.urlopen(url))
    points = []
    features = data['features']
    names = []
    for p in data['features']:
        for d in p['properties']:
            print d
            var =  p['properties'][''+d]
            print var


