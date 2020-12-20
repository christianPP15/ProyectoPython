from tkinter import messagebox

import random
from Modelos import Ticket, Vehiculos
from Repositorios import ClienteRepository
from Servicios import db, PlazaServicio, TicketServicio, GeneracionPDF
import datetime

def depositarVehiculo(tipo,matricula):
    if tipo==1:
        vehiculo= Vehiculos.Turismo(matricula=matricula)
        tipo="Turismo"
    elif tipo==2:
        vehiculo=Vehiculos.Motocicleta(matricula=matricula)
        tipo="Moto"
    else:
        vehiculo=Vehiculos.MovilidadReducida(matricula=matricula)
        tipo="Movilidad reducida"
    plazaOcupar= PlazaServicio.darPlazaLibreTipo(tipo)
    if plazaOcupar!=-1:
        PlazaServicio.ocuparPlaza(plazaOcupar)
        db.session.add(vehiculo)
        ticket= Ticket.Ticket(vehiculo=vehiculo, plaza=plazaOcupar, coste=0, pin=random.randint(111111, 999999), fechaEntrada=datetime.datetime.now(), fechaSalida=None)
        GeneracionPDF.crearPDF(ticket)
        db.session.add(ticket)
        db.session.commit()
        return TicketServicio.pintarTicket(ticket)
    else:
        return f"Imposible realizar la operación, sin plazas disponibles para {tipo}"


def retirarVehiculo(matricula,pin,identificador):
    ticket= TicketServicio.buscarTicketRetirada(pin, matricula, identificador)
    if ticket!=-1:
        if ticket.coste==0:
            plaza=ticket.plaza
            ticket.fechaSalida=datetime.datetime.now()
            if isinstance(ticket.vehiculo,Vehiculos.Turismo):
                costeMinimo=0.12
            elif isinstance(ticket.vehiculo,Vehiculos.Motocicleta):
                costeMinimo=0.08
            else:
                costeMinimo=0.1
            precio=round(((ticket.fechaSalida-ticket.fechaEntrada).total_seconds() / 60)*costeMinimo,2)
            ticket.coste=precio
            messagebox.showinfo(message=f"Debes pagar un total de {precio}", title="Pago")
            db.session.add(ticket)
            PlazaServicio.liberarPlaza(plaza)
            db.session.add(plaza)
            db.session.commit()
            return "Operacion completada con exito"
        else:
            return "El vehículo ya fue retirado anteriormente"
    else:
        return "No existen registros con esos datos"



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
