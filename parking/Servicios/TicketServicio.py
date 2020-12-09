from Repositorios import TicketRepository
import datetime
def pintarTicket(ticket):
    TicketRepository.pintarTicket(ticket)

def buscarTicketRetirada(pin,matricula,identificador):
    return TicketRepository.buscarTicketRetirada(pin,matricula,identificador)

def facturacion():
    tickets=TicketRepository.devolverFacturasConFechaFinalEntreDosFechas()
    cantidad=0
    for ticket in tickets:
        cantidad+=ticket.coste
    print(f"Existen un total de {len(tickets)} facturas entre las fechas solicitadas, por las cuales se ha obtenido un beneficio de {cantidad}")
