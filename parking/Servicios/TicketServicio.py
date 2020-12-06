from Repositorios import TicketRepository

def pintarTicket(ticket):
    TicketRepository.pintarTicket(ticket)

def buscarTicketRetirada(tickets,pin,matricula,identificador):
    return TicketRepository.buscarTicketRetirada(tickets,pin,matricula,identificador)
