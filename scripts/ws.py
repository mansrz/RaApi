from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import

class MateriaPorAula():
    id = 0
    def __init__(self, nombre, codMat, HInicio,HFin, Dia, Aula, Bloque, Campus, BloqueCampus):
        self.Nombre=nombre
        self.CodMat=codMat
        self.HInicio=HInicio
        self.HFin=HFin
        self.Dia=Dia
        self.Aula=Aula
        self.Bloque=Bloque
        self.Campus=Campus
        self.BloqueCampus=BloqueCampus

def ObtenerMateriasxAula(idaula):
    url = 'http://ws.espol.edu.ec/saac/wsandroid.asmx?WSDL'
    imp = Import('http://www.w3.org/2001/XMLSchema') # the schema to import.
    imp.filter.add('http://tempuri.org/')
    doctor = ImportDoctor(imp)
    client = Client(url, doctor=doctor)
    mxa = client.service.wsMateriasAulas(idaula)
    i=0
    for i in mxa[1].__getitem__(0).__getitem__(0):
        Nombre = i.__getitem__(2)
        CodigoMateria = i.__getitem__(3)
        HoraInicio = i.__getitem__(4)
        HoraFin = i.__getitem__(5)
        NombreDia = i.__getitem__(6)
        Aula = i.__getitem__(7)
        Bloque = i.__getitem__(8)
        Campus = i.__getitem__(9)
        BloqueCampus = i.__getitem__(10)
        ma = MateriaPorAula(Nombre,CodigoMateria,HoraInicio,HoraFin,NombreDia,Aula,Bloque,Campus,BloqueCampus)
    return ma

def utf8ify_s(s):
    if isinstance(s, unicode):
        return s.encode('utf-8')
    else:
        return str(s)

def convert(d):
    from django.utils.encoding import smart_str, smart_unicode
    return smart_str(d)

def getall():
    IdsAulas=[100,101,102,103,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,266,267,607,658]
    lista = []
    for i in IdsAulas:
        lista.append(ObtenerMateriasxAula(i))
    return lista

from Web.models import Schedule
def save_all(d):
    for i in d:
	sc = Schedule()
	sc.name = convert(i.Nombre)
	sc.codmat = convert(i.CodMat)
	sc.hora_inicio = convert(i.HInicio)
	sc.hora_fin = convert(i.HFin)
	sc.dia = convert(i.Dia)
	sc.aula = convert(i.Aula)
	sc.bloque = convert(i.Bloque)
	sc.campus = convert(i.Campus)
	sc.bloquecampus = convert(i.BloqueCampus)
	sc.save()

