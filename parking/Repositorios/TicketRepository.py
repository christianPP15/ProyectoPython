def pintarTicket(ticket):
    print("------------------------------")
    print(f"Entrada -> {ticket.fechaEntrada}")
    print(f"PIN -> {ticket.pin}")
    print(f"Identificador de la plaza {ticket.plaza.identificador}")
    print("------------------------------")


def buscarTicketRetirada(tickets, pin, matricula, identificador):
    for i in tickets:
        if i.pin == pin and i.matricula == matricula and i.plaza.identificador == identificador:
            return i
    return -1
