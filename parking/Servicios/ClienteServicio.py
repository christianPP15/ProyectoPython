from Servicios import PlazaServicio
import random
from Modelos import Vehiculos
from Modelos import Ticket
from Servicios import TicketServicio
from Repositorios import ClienteRepository
from Servicios import db
import datetime

def reservarPlaza():
    tipo=int(input("1.Turismo\t"
           "2.Motocicleta\t"
           "3.Movilidad reducida"))
    while tipo>3 or tipo<=0:
        tipo=int(input("1.Turismo\t"
           "2.Motocicleta\t"
           "3.Movilidad reducida"))
    if tipo==1:
        tipo="Turismo"
    elif tipo==2:
        tipo="Moto"
    else:
        tipo="Movilidad reducida"
    plazaOcupar=PlazaServicio.darPlazaLibreTipo(tipo)
    if plazaOcupar!=-1:
        PlazaServicio.ocuparPlaza(plazaOcupar)
        matricula=input("Introduce la matricula de su vehículo")
        vehiculo=Vehiculos.Vehiculos(matricula=matricula,tipo=tipo)
        db.session.add(vehiculo)
        ticket=Ticket.Ticket(vehiculo=vehiculo,plaza=plazaOcupar,coste=0,pin=random.randint(111111,999999),fechaEntrada=datetime.datetime.now(),fechaSalida=None)
        db.session.add(ticket)
        TicketServicio.pintarTicket(ticket)
        db.session.commit()
    else:
        print(f"Imposible realizar la operación, sin plazas disponibles para {tipo}")


def retirarVehiculo():
    matricula=input("Introduce la matricula de su vehículo")
    pin=int(input("Introduce el pin asignado"))
    identificador=input("Introduce el identificador de la plaza")
    ticket=TicketServicio.buscarTicketRetirada(pin,matricula,identificador)
    if ticket!=-1:
        plaza=ticket.plaza
        ticket.fechaSalida=datetime.datetime.now()
        precio=round(((ticket.fechaSalida-ticket.fechaEntrada).total_seconds() / 60)*ticket.plaza.coste_minimo,2)
        ticket.coste=precio
        ClienteRepository.pago(ticket.coste)
        db.session.add(ticket)
        PlazaServicio.liberarPlaza(plaza)
        db.session.add(plaza)
        db.session.commit()
        print("Gracias por contar con nosotros")
    else:
        print("Ticket no encontrado")



def buscarClientePorAbono(abono):
    return ClienteRepository.buscarClientePorAbono(abono)

def depositarAbonados():
    matricula=input("Introduzca la matricula de su vehículo")
    dni=input("Introduzca su dni")
    cliente=ClienteRepository.buscarClientePorDniMatricula(dni,matricula)
    PlazaServicio.ocuparPlaza(cliente.abono.plaza)
    db.session.add(cliente.abono.plaza)
    db.session.commit()
    print("Vehículo guardado correctamente, recuerde que su pin es: "+str(cliente.abono.pin))

def retirarAbono():
    matricula=input("Introduzca la matricula de su vehículo")
    dni=input("Introduzca su dni")
    pin=input("Introduzca el pin")
    cliente=ClienteRepository.buscarClientePorDniPinMatricula(dni,matricula,pin)
    PlazaServicio.liberarPlaza(cliente.abono.plaza)
    db.session.add(cliente.abono.plaza)
    db.session.commit()
    print("Gracias por usar nuestros servicios")

def buscarClientePorDniMatricula(dni,matricula):
    return ClienteRepository.buscarClientePorDniMatricula(dni,matricula)
def buscarClientePorDniPinMatricula(dni,matricula,pin):
    return ClienteRepository.buscarClientePorDniPinMatricula(dni,matricula,pin)
