from Repositorios import TicketRepository


def pintarTicket(ticket):
    return TicketRepository.pintarTicket(ticket)

def buscarTicketRetirada(pin,matricula,identificador):
    return TicketRepository.buscarTicketRetirada(pin, matricula, identificador)

def facturacion(anio1,mes1,dia1,anio2,mes2,dia2):
    tickets= TicketRepository.devolverFacturasConFechaFinalEntreDosFechas(anio1, mes1, dia1, anio2, mes2, dia2)
    cantidad=0
    for ticket in tickets:
        cantidad+=ticket.coste
    return f"Existen un total de {len(tickets)} facturas entre las fechas solicitadas, por las cuales se ha obtenido un beneficio de {round(cantidad,2)}"
