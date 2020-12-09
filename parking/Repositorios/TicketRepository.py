from Servicios import db
from Modelos import Ticket,Vehiculos,Plaza
import datetime
def pintarTicket(ticket):
    print("------------------------------")
    print(f"Entrada -> {ticket.fechaEntrada}")
    print(f"PIN -> {ticket.pin}")
    print(f"Identificador de la plaza {ticket.plaza.identificador}")
    print("------------------------------")


def buscarTicketRetirada( pin, matricula, identificador):
    ticket=db.session.query(Ticket.Ticket).join(Vehiculos.Vehiculos).join(Plaza.Plaza).filter(
        Vehiculos.Vehiculos._Vehiculos__matricula==matricula
    ).filter(
        Ticket.Ticket._Ticket__pin==pin
    ).filter(
        Plaza.Plaza._Plaza__identificador==identificador
    ).first()
    if ticket:
        return ticket
    else:
        return -1

def devolverTodosLosTicketsTerminados():
    return db.session.query(Ticket.Ticket).filter(
        Ticket.Ticket._Ticket__coste>0
    )


def devolverFacturasConFechaFinalEntreDosFechas():
    fecha1=datetime.datetime.now()
    fecha2=datetime.datetime.now()
    comprobados=[]
    anio1=int(input("Introduce el año de la primera fecha"))
    mes1=int(input("Introduce el mes de la primera fecha"))
    dia1=int(input("Introduce el día de la primera fecha"))
    fecha_limite_inferior=fecha1.replace(year=anio1,month=mes1,day=dia1)
    anio2=int(input("Introduce el año de la segunda fecha"))
    mes2=int(input("Introduce el mes de la segunda fecha"))
    dia2=int(input("Introduce el día de la segunda fecha"))
    fecha_limite_superior=fecha2.replace(year=anio2,month=mes2,day=dia2)
    tickets=devolverTodosLosTicketsTerminados()
    for ticket in tickets:
        fecha_comprobar=ticket.fechaSalida
        if fecha_comprobar.year>=fecha_limite_inferior.year and fecha_comprobar.year<=fecha_limite_superior.year and fecha_comprobar.month>=fecha_limite_inferior.month and fecha_comprobar.month<=fecha_limite_superior.month and fecha_comprobar.day>=fecha_limite_inferior.day and fecha_comprobar.day<=fecha_limite_superior.day:
            comprobados.append(ticket)
    return comprobados
