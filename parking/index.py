from Modelos import Parking
from Servicios import ParkingServicio
from Servicios import PlazaServicio
from Servicios import TicketServicio
from Modelos import  Ticket
from Modelos import Plaza
from Modelos import Abono
from Modelos import Vehiculos
from Modelos import Clientes
from Servicios import db
import datetime
import random
from Servicios import ClienteServicio
'''def run():
    vehiculo=Vehiculos.Vehiculos('addadawd','dadawdawd')
    db.session.add(vehiculo)
    db.session.commit()'''

if __name__=='__main__':
    db.Base.metadata.drop_all(db.engine)
    db.Base.metadata.create_all(db.engine)

t = datetime.timedelta(days=14, hours=4, seconds=1000)
fecha1=datetime.datetime.now()
fecha2=datetime.datetime.now()
fecha2=fecha2+t
vehiculo=Vehiculos.Vehiculos(matricula='addadawd',tipo='dadawdawd')
plaza=Plaza.Plaza(identificador='l1',tipo='Turismo',coste_minimo=32,ocupado=False)
ticket=Ticket.Ticket(fechaEntrada=fecha1,fechaSalida=fecha2,pin=2132,matricula='wadawdawd',coste=34,plaza=plaza)
abono=Abono.Abono(fechaInicial=datetime.datetime.now(),fechaFinal=datetime.datetime.now(),precio=32.3,pin=232323)
cliente=Clientes.Cliente(nombre="Christian",apellidos="Payo Parra",vehiculo=vehiculo,abono=abono)
db.session.add(abono)
db.session.add(plaza)
db.session.add(ticket)
db.session.add(vehiculo)
db.session.add(cliente)
db.session.commit()
parking=Parking.Parking()
tickets=[]
ParkingServicio.mostrarDisponibilidad(parking)

#ClienteServicio.reservarPlaza(parking,tickets)


#ClienteServicio.retirarVehiculo(parking,tickets)
vehiculo = db.session.query(Vehiculos.Vehiculos).all()
tickets1=db.session.query(Ticket.Ticket).all()
clientes=db.session.query(Clientes.Cliente).all()
plazas=db.session.query(Plaza.Plaza).all()
abonos=db.session.query(Abono.Abono).all()
for i in vehiculo:
    print(i)
for i in tickets1:
    print(i)
for i in clientes:
    print(i)
for i in plazas:
    print(i)
for i in abonos:
    print(i)
print(parking)
