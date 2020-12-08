from Servicios import PlazaServicio
from Modelos import Vehiculos
from Modelos import  Ticket
from Servicios import TicketServicio
import datetime

def reservarPlaza():
    tipo=int(input("1.Turismo\t"
           "2.Motocicleta\t"
           "3.Movilidad reducida"))
    if tipo==1:
        tipo="Turismo"
    elif tipo==2:
        tipo="Moto"
    else:
        tipo="Movilidad reducida"
    plazaOcupar=PlazaServicio.darPlazaLibreTipo(tipo)
    if plazaOcupar!=-1:
        PlazaServicio.ocuparPlaza(plazaOcupar)
        #matricula=input("Introduce la matricula de su vehículo")
        #vehiculo=Vehiculos.Vehiculos(matricula,tipo)
        #ticket=Ticket.Ticket(vehiculo.matricula,plazaOcupar)
        #TicketServicio.pintarTicket(ticket)
        #tickets.append(ticket)
    else:
        print(f"Imposible realizar la operación, sin plazas disponibles para {tipo}")


# def retirarVehiculo(parking,tickets):
#     matricula=input("Introduce la matricula de su vehículo")
#     pin=int(input("Introduce el pin asignado"))
#     identificador=input("Introduce el identificador de la plaza")
#     ticket=TicketServicio.buscarTicketRetirada(tickets,pin,matricula,identificador)
#     ticket.fechaSalida=datetime.datetime.now()
#     ticket.coste=((ticket.fechaSalida-ticket.fechaEntrada).total_seconds() / 60)*ticket.plaza.coste_minimo
#     pago(ticket.coste)
#
#     print("Gracias por contar con nosotros")
#
# def pago(coste):
#     print(f"El precio a pagar es de: {coste}")
#     dinero=float(input("Introduce la cantidad a pagar: "))
#     while dinero<coste:
#         print("Error con su pago, intentelo de nuevo")
#         dinero=float(input("Introduce la cantidad a pagar: "))
#     print(f"Gracias por el pago, el cambio es de : {dinero-coste}")
#
#
