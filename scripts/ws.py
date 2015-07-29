from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import
import mysql.connector

class Conexion():
   user = 'root'
   pwd = '1234'
   host = '127.0.0.1'
   port = '3306'
   database = 'CHICHODB'
   def getConnection(self):
       conexion= mysql.connector.connect(user=self.user, password=self.pwd,host=self.host,database=self.database,port=self.port)
       return conexion

class MateriaPorAula():
    conexion = Conexion()
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

    def contar(self):
        query = ('SELECT id from MateriaPorAula order by id desc limit 1;')
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.execute(query)
        result=cursor.fetchone()
        cursor.close()
        if result is None:
            return 1
        return (result[0]+1)

    def ingresar(self):
        oper= 'INSERT INTO MateriaPorAula (id,Nombre,CodMat,HInicio,HFin,Dia,Aula,Bloque,Campus,BloqueCampus) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.execute(oper,(str(self.contar()), str(self.Nombre),str(self.CodMat),str(self.HInicio),str(self.HFin), str(self.Dia), str(self.Aula), str(self.Bloque), str(self.Campus), str(self.BloqueCampus)))
        conexion.commit()
        cursor.close()

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
        ma=MateriaPorAula(Nombre,CodigoMateria,HoraInicio,HoraFin,NombreDia,Aula,Bloque,Campus,BloqueCampus)
        ma.ingresar()

IdsAulas=[100,101,102,103,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,266,267,607,658]
conexion = Conexion().getConnection()
cursor= conexion.cursor()
cursor.execute('Delete from MateriaPorAula')
conexion.commit()
cursor.close()
for i in IdsAulas:
    ObtenerMateriasxAula(i)
