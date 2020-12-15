from tkinter import messagebox

import random
from Modelos import Ticket, Vehiculos
from Repositorios import ClienteRepository
from Servicios import db, PlazaServicio, TicketServicio
import datetime

def depositarVehiculo(tipo,matricula):
    if tipo==1:
        tipo="Turismo"
    elif tipo==2:
        tipo="Moto"
    else:
        tipo="Movilidad reducida"
    plazaOcupar= PlazaServicio.darPlazaLibreTipo(tipo)
    if plazaOcupar!=-1:
        PlazaServicio.ocuparPlaza(plazaOcupar)
        vehiculo= Vehiculos.Vehiculos(matricula=matricula, tipo=tipo)
        db.session.add(vehiculo)
        ticket= Ticket.Ticket(vehiculo=vehiculo, plaza=plazaOcupar, coste=0, pin=random.randint(111111, 999999), fechaEntrada=datetime.datetime.now(), fechaSalida=None)
        db.session.add(ticket)
        db.session.commit()
        return TicketServicio.pintarTicket(ticket)
    else:
        print(f"Imposible realizar la operación, sin plazas disponibles para {tipo}")


def retirarVehiculo(matricula,pin,identificador):
    ticket= TicketServicio.buscarTicketRetirada(pin, matricula, identificador)
    if ticket!=-1:
        plaza=ticket.plaza
        ticket.fechaSalida=datetime.datetime.now()
        precio=round(((ticket.fechaSalida-ticket.fechaEntrada).total_seconds() / 60)*ticket.plaza.coste_minimo,2)
        ticket.coste=precio
        messagebox.showinfo(message=f"Debes pagar un total de {precio}", title="Pago")
        db.session.add(ticket)
        PlazaServicio.liberarPlaza(plaza)
        db.session.add(plaza)
        db.session.commit()
        return True
    else:
        return False



def buscarClientePorAbono(abono):
    return ClienteRepository.buscarClientePorAbono(abono)

def depositarAbonados(matricula,dni):
    try:
        cliente= ClienteRepository.buscarClientePorDniMatricula(dni, matricula)
        PlazaServicio.ocuparPlaza(cliente.abono.plaza)
        db.session.add(cliente.abono.plaza)
        db.session.commit()
        return "Vehículo guardado correctamente, recuerde que su pin es: "+str(cliente.abono.pin)
    except :
        return "No encontramos existencias para los datos especificados"

def retirarAbono(matricula,dni,pin):
    try:
        cliente= ClienteRepository.buscarClientePorDniPinMatricula(dni, matricula, pin)
        PlazaServicio.liberarPlaza(cliente.abono.plaza)
        db.session.add(cliente.abono.plaza)
        db.session.commit()
        return "Gracias por usar nuestros servicios"
    except:
        return "No se encuentran datos con esa información"

def buscarClientePorDniMatricula(dni,matricula):
    return ClienteRepository.buscarClientePorDniMatricula(dni, matricula)
def buscarClientePorDniPinMatricula(dni,matricula,pin):
    return ClienteRepository.buscarClientePorDniPinMatricula(dni, matricula, pin)
