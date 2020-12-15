from Servicios import db
from Modelos import Plaza, Ticket, Vehiculos
import datetime
def pintarTicket(ticket):
    return f"------------------------------\n" \
           f"Entrada -> {ticket.fechaEntrada.year}/{ticket.fechaEntrada.month}/{ticket.fechaEntrada.day} {ticket.fechaEntrada.hour}:{ticket.fechaEntrada.minute}:{ticket.fechaEntrada.second}\n" \
           f"PIN -> {ticket.pin}\n" \
           f"Identificador de la plaza {ticket.plaza.identificador}\n" \
           f"------------------------------"




def buscarTicketRetirada( pin, matricula, identificador):
    ticket= db.session.query(Ticket.Ticket).join(Vehiculos.Vehiculos).join(Plaza.Plaza).filter(
        Vehiculos.Vehiculos._Vehiculos__matricula == matricula
    ).filter(
        Ticket.Ticket._Ticket__pin == pin
    ).filter(
        Plaza.Plaza._Plaza__identificador == identificador
    ).first()
    if ticket:
        return ticket
    else:
        return -1

def devolverTodosLosTicketsTerminados():
    return db.session.query(Ticket.Ticket).filter(
        Ticket.Ticket._Ticket__coste > 0
    )


def devolverFacturasConFechaFinalEntreDosFechas(anio1,mes1,dia1,anio2,mes2,dia2):
    fecha1=datetime.datetime.now()
    fecha2=datetime.datetime.now()
    comprobados=[]
    fecha_limite_inferior=fecha1.replace(year=anio1,month=mes1,day=dia1)
    fecha_limite_superior=fecha2.replace(year=anio2,month=mes2,day=dia2)
    tickets=devolverTodosLosTicketsTerminados()
    for ticket in tickets:
        fecha_comprobar=ticket.fechaSalida
        if fecha_comprobar.year>=fecha_limite_inferior.year and fecha_comprobar.year<=fecha_limite_superior.year and fecha_comprobar.month>=fecha_limite_inferior.month and fecha_comprobar.month<=fecha_limite_superior.month and fecha_comprobar.day>=fecha_limite_inferior.day and fecha_comprobar.day<=fecha_limite_superior.day:
            comprobados.append(ticket)
    return comprobados
