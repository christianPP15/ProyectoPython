from Servicios import db
from Modelos import Ticket,Vehiculos,Plaza
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
