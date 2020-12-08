from Repositorios import TicketRepository

def pintarTicket(ticket):
    TicketRepository.pintarTicket(ticket)

def buscarTicketRetirada(pin,matricula,identificador):
    return TicketRepository.buscarTicketRetirada(pin,matricula,identificador)
